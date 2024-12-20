from typing import Dict, List, Optional, Union, Tuple
from datetime import datetime
import logging
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import PyMongoError
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

logger = logging.getLogger(__name__)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'vector_nexus')
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

class DatabaseError(Exception):
    """Base exception for database operations"""
    pass

def get_mongo_connection():
    """
    Establish a connection to the MongoDB database.
    
    Returns:
        MongoDB database connection
    
    Raises:
        DatabaseError: If connection fails
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        # Test connection
        db.command('ping')
        return db
    except PyMongoError as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise DatabaseError(f"Database connection failed: {e}")

def insert_document(document: Dict) -> str:
    """
    Insert a new document into MongoDB.
    
    Args:
        document: Document to insert
    
    Returns:
        str: ID of the inserted document
    
    Raises:
        DatabaseError: If insertion fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        
        # Add metadata
        document.update({
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        })
        
        result = documents.insert_one(document)
        return str(result.inserted_id)
    except PyMongoError as e:
        logger.error(f"Failed to insert document: {e}")
        raise DatabaseError(f"Document insertion failed: {e}")

def get_document(document_id: Union[str, ObjectId]) -> Optional[Dict]:
    """
    Retrieve a document from MongoDB by its ID.
    
    Args:
        document_id: Document ID
    
    Returns:
        Optional[Dict]: Document if found, None otherwise
    
    Raises:
        DatabaseError: If retrieval fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        document = documents.find_one({"_id": ObjectId(str(document_id))})
        return document
    except PyMongoError as e:
        logger.error(f"Failed to get document {document_id}: {e}")
        raise DatabaseError(f"Document retrieval failed: {e}")

def update_document(document_id: Union[str, ObjectId], update_data: Dict) -> bool:
    """
    Update a document in MongoDB by its ID.
    
    Args:
        document_id: Document ID
        update_data: Data to update
    
    Returns:
        bool: True if document was updated, False if not found
    
    Raises:
        DatabaseError: If update fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        
        # Add update timestamp
        update_data['updated_at'] = datetime.utcnow()
        
        result = documents.update_one(
            {"_id": ObjectId(str(document_id))},
            {"$set": update_data}
        )
        return result.modified_count > 0
    except PyMongoError as e:
        logger.error(f"Failed to update document {document_id}: {e}")
        raise DatabaseError(f"Document update failed: {e}")

def delete_document(document_id: Union[str, ObjectId]) -> bool:
    """
    Delete a document from MongoDB by its ID.
    
    Args:
        document_id: Document ID
    
    Returns:
        bool: True if document was deleted, False if not found
    
    Raises:
        DatabaseError: If deletion fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        result = documents.delete_one({"_id": ObjectId(str(document_id))})
        return result.deleted_count > 0
    except PyMongoError as e:
        logger.error(f"Failed to delete document {document_id}: {e}")
        raise DatabaseError(f"Document deletion failed: {e}")

def list_documents(
    page: int = 1,
    per_page: int = DEFAULT_PAGE_SIZE,
    status: Optional[str] = None,
    sort_by: str = 'created_at',
    sort_order: str = 'desc'
) -> Tuple[List[Dict], int]:
    """
    List documents from MongoDB with pagination and filtering.
    
    Args:
        page: Page number (1-based)
        per_page: Number of items per page
        status: Filter by document status
        sort_by: Field to sort by
        sort_order: Sort order ('asc' or 'desc')
    
    Returns:
        Tuple[List[Dict], int]: List of documents and total count
    
    Raises:
        DatabaseError: If listing fails
        ValueError: If pagination parameters are invalid
    """
    try:
        # Validate pagination parameters
        if page < 1:
            raise ValueError("Page must be greater than 0")
        if per_page < 1:
            raise ValueError("Items per page must be greater than 0")
        if per_page > MAX_PAGE_SIZE:
            per_page = MAX_PAGE_SIZE

        db = get_mongo_connection()
        documents = db.documents

        # Build query
        query = {}
        if status:
            query['status'] = status

        # Calculate skip and limit
        skip = (page - 1) * per_page

        # Determine sort order
        sort_direction = ASCENDING if sort_order.lower() == 'asc' else DESCENDING

        # Get total count
        total_count = documents.count_documents(query)

        # Get paginated results
        cursor = documents.find(query) \
            .sort(sort_by, sort_direction) \
            .skip(skip) \
            .limit(per_page)

        # Convert ObjectId to string in results
        results = []
        for doc in cursor:
            doc['_id'] = str(doc['_id'])
            results.append(doc)

        return results, total_count

    except ValueError as e:
        raise
    except PyMongoError as e:
        logger.error(f"Failed to list documents: {e}")
        raise DatabaseError(f"Document listing failed: {e}")

def count_documents(status: Optional[str] = None) -> int:
    """
    Count documents in MongoDB with optional status filter.
    
    Args:
        status: Filter by document status
    
    Returns:
        int: Number of documents
    
    Raises:
        DatabaseError: If counting fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        query = {'status': status} if status else {}
        return documents.count_documents(query)
    except PyMongoError as e:
        logger.error(f"Failed to count documents: {e}")
        raise DatabaseError(f"Document counting failed: {e}")

def create_indexes():
    """
    Create indexes for the documents collection.
    
    Raises:
        DatabaseError: If index creation fails
    """
    try:
        db = get_mongo_connection()
        documents = db.documents
        
        # Create indexes
        documents.create_index([('created_at', DESCENDING)])
        documents.create_index([('status', ASCENDING)])
        documents.create_index([('title', ASCENDING)])
        
        logger.info("Database indexes created successfully")
    except PyMongoError as e:
        logger.error(f"Failed to create indexes: {e}")
        raise DatabaseError(f"Index creation failed: {e}")
