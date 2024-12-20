from typing import Dict, List, Optional, Union
from datetime import datetime
import logging
import os
import asyncio
from bson.objectid import ObjectId

from flask import Flask, request, jsonify, render_template, Response
from flask.typing import ResponseReturnValue

from backend.database import (
    get_mongo_connection, 
    insert_document, 
    get_document, 
    update_document, 
    delete_document, 
    list_documents
)
from backend.redis_utils import get_task_queue, get_redis_connection
from backend.embeddings import EmbeddingsGenerator
from backend.tasks import process_document
from backend.qdrant_utils import search_points

app = Flask(__name__, template_folder='templates', static_folder='static')
logger = logging.getLogger(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

embeddings_generator = EmbeddingsGenerator()

def error_response(message: str, status_code: int = 500) -> ResponseReturnValue:
    """Create a standardized error response"""
    return jsonify({
        'error': message,
        'timestamp': datetime.utcnow().isoformat()
    }), status_code

@app.route('/api/documents', methods=['GET'])
def list_documents_route() -> ResponseReturnValue:
    """List all documents with optional filtering and pagination"""
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        status = request.args.get('status')
        sort_by = request.args.get('sort_by', 'created_at')
        sort_order = request.args.get('sort_order', 'desc')

        # Validate parameters
        if page < 1:
            return error_response("Page must be greater than 0", 400)
        if per_page < 1:
            return error_response("Items per page must be greater than 0", 400)
        if sort_order not in ['asc', 'desc']:
            return error_response("Sort order must be 'asc' or 'desc'", 400)

        # Get documents with pagination
        documents, total_count = list_documents(
            page=page,
            per_page=per_page,
            status=status,
            sort_by=sort_by,
            sort_order=sort_order
        )

        # Calculate pagination metadata
        total_pages = (total_count + per_page - 1) // per_page
        has_next = page < total_pages
        has_prev = page > 1

        return jsonify({
            'documents': documents,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total_items': total_count,
                'total_pages': total_pages,
                'has_next': has_next,
                'has_prev': has_prev
            },
            'filters': {
                'status': status,
                'sort_by': sort_by,
                'sort_order': sort_order
            }
        }), 200

    except ValueError as e:
        return error_response(str(e), 400)
    except Exception as e:
        logger.error(f"Error listing documents: {e}", exc_info=True)
        return error_response("Failed to list documents")

@app.route('/api/documents', methods=['POST'])
async def upload_document() -> ResponseReturnValue:
    """Upload and process a new document"""
    try:
        # Validate request
        if not request.is_json:
            return error_response("Content-Type must be application/json", 400)
            
        data = request.get_json()
        title = data.get('title', '').strip()
        content = data.get('content', '').strip()

        if not title or not content:
            return error_response("Title and content are required and cannot be empty", 400)

        # Store document in MongoDB
        doc = {
            "title": title,
            "content": content,
            "status": "pending",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        mongo_id = insert_document(doc)

        # Get Redis connections
        task_queue = get_task_queue()
        redis_conn = get_redis_connection()
        
        if not task_queue or not redis_conn:
            logger.error("Failed to connect to Redis/RQ")
            update_document(mongo_id, {"status": "error", "error_message": "Task queue unavailable"})
            return error_response("Service temporarily unavailable", 503)

        # Enqueue processing task
        task = task_queue.enqueue(
            process_document,
            args=(str(mongo_id), title, content),
            job_timeout='10m'
        )
        
        # Allow some time for the task to start
        await asyncio.sleep(0.1)

        return jsonify({
            'id': str(mongo_id),
            'title': title,
            'status': 'pending',
            'message': 'Document uploaded and queued for processing'
        }), 201

    except Exception as e:
        logger.error(f"Error uploading document: {e}", exc_info=True)
        return error_response("Failed to upload document")

@app.route('/api/documents/<string:doc_id>', methods=['GET'])
def get_document_route(doc_id: str) -> ResponseReturnValue:
    """Get a specific document by ID"""
    try:
        doc = get_document(doc_id)
        if not doc:
            return error_response("Document not found", 404)

        return jsonify({
            'id': str(doc['_id']),
            'title': doc['title'],
            'content': doc['content'],
            'status': doc['status'],
            'created_at': doc.get('created_at'),
            'updated_at': doc.get('updated_at'),
            'processed_at': doc.get('processed_at'),
            'error_message': doc.get('error_message'),
            'processing_time': doc.get('processing_time')
        }), 200

    except Exception as e:
        logger.error(f"Error getting document {doc_id}: {e}", exc_info=True)
        return error_response(f"Failed to get document {doc_id}")

@app.route('/api/documents/<string:doc_id>', methods=['PUT'])
async def update_document_route(doc_id: str) -> ResponseReturnValue:
    """Update a specific document"""
    try:
        if not request.is_json:
            return error_response("Content-Type must be application/json", 400)
            
        data = request.get_json()
        
        # Validate update data
        if 'title' in data and not data['title'].strip():
            return error_response("Title cannot be empty", 400)
        if 'content' in data and not data['content'].strip():
            return error_response("Content cannot be empty", 400)

        # Add update metadata
        data['updated_at'] = datetime.utcnow()
        
        # Perform update
        updated = update_document(doc_id, data)
        if not updated:
            return error_response("Document not found", 404)

        # If content was updated, reprocess the document
        if 'content' in data:
            task_queue = get_task_queue()
            if task_queue:
                task_queue.enqueue(
                    process_document,
                    args=(doc_id, data.get('title'), data['content']),
                    job_timeout='10m'
                )
                await asyncio.sleep(0.1)

        return jsonify({
            'message': 'Document updated successfully',
            'reprocessing': 'content' in data
        }), 200

    except Exception as e:
        logger.error(f"Error updating document {doc_id}: {e}", exc_info=True)
        return error_response(f"Failed to update document {doc_id}")

@app.route('/api/documents/<string:doc_id>', methods=['DELETE'])
def delete_document_route(doc_id: str) -> ResponseReturnValue:
    """Delete a specific document"""
    try:
        deleted = delete_document(doc_id)
        if not deleted:
            return error_response("Document not found", 404)

        return jsonify({
            'message': 'Document deleted successfully',
            'id': doc_id
        }), 200

    except Exception as e:
        logger.error(f"Error deleting document {doc_id}: {e}", exc_info=True)
        return error_response(f"Failed to delete document {doc_id}")

@app.route('/api/search', methods=['POST'])
def search_documents() -> ResponseReturnValue:
    """Search for documents using semantic search"""
    try:
        # Validate request
        if not request.is_json:
            return error_response("Content-Type must be application/json", 400)

        data = request.get_json()
        query = data.get('query', '').strip()
        limit = data.get('limit', 10)
        score_threshold = data.get('score_threshold')
        filter_condition = data.get('filter')

        # Validate parameters
        if not query:
            return error_response("Query is required", 400)
        if limit < 1:
            return error_response("Limit must be greater than 0", 400)

        # Generate embeddings for the query
        try:
            query_vector = embeddings_generator.generate_embeddings(query)
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}", exc_info=True)
            return error_response("Failed to process search query")

        # Search in Qdrant
        search_results = search_points(
            collection_name='documents',
            vector=query_vector,
            limit=limit,
            score_threshold=score_threshold,
            filter_condition=filter_condition
        )

        if search_results is None:
            return error_response("Search failed", 500)

        # Format and return results
        formatted_results = []
        for result in search_results.get('result', []):
            payload = result.get('payload', {})
            formatted_results.append({
                'id': payload.get('document_id'),
                'title': payload.get('title'),
                'content': payload.get('content'),
                'score': result.get('score', 0),
                'metadata': {
                    'status': payload.get('status'),
                    'created_at': payload.get('created_at'),
                    'updated_at': payload.get('updated_at')
                }
            })

        return jsonify({
            'query': query,
            'results': formatted_results,
            'total': len(formatted_results),
            'search_params': {
                'limit': limit,
                'score_threshold': score_threshold,
                'filter': filter_condition
            }
        }), 200

    except ValueError as e:
        return error_response(str(e), 400)
    except Exception as e:
        logger.error(f"Error during search: {e}", exc_info=True)
        return error_response("Search failed")

@app.errorhandler(404)
def not_found(e) -> ResponseReturnValue:
    """Handle 404 errors"""
    return error_response("Resource not found", 404)

@app.errorhandler(405)
def method_not_allowed(e) -> ResponseReturnValue:
    """Handle 405 errors"""
    return error_response(f"Method {request.method} not allowed", 405)

@app.errorhandler(500)
def server_error(e) -> ResponseReturnValue:
    """Handle 500 errors"""
    logger.error(f"Server error: {e}", exc_info=True)
    return error_response("Internal server error")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
