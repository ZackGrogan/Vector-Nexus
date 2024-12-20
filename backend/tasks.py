from typing import Optional, Union
from datetime import datetime
import logging
from bson import ObjectId

from backend.embeddings import EmbeddingsGenerator
import backend.qdrant_utils as qdrant_utils
from backend.database import update_document, get_document
from backend.gemini_utils import clean_text_with_gemini

logger = logging.getLogger(__name__)

embeddings_generator = EmbeddingsGenerator()

async def process_document(mongo_id: Union[str, ObjectId], title: str, content: str) -> bool:
    """
    Process a document by cleaning its content and generating embeddings.
    
    Args:
        mongo_id: MongoDB document ID
        title: Document title
        content: Document content
    
    Returns:
        bool: True if processing succeeded, False otherwise
    """
    mongo_id = str(mongo_id)
    start_time = datetime.utcnow()
    
    try:
        # Update status to processing
        update_document(mongo_id, {
            "status": "processing",
            "processing_started_at": start_time,
            "error_message": None
        })

        # Input validation
        if not content or not title:
            raise ValueError("Content and title are required")

        # Validate content with Gemini
        logger.info(f"Cleaning content for document {mongo_id}")
        cleaned_content = await clean_text_with_gemini(content)
        if not cleaned_content:
            raise ValueError("Failed to validate content with Gemini")

        # Generate embedding with fallback strategy
        logger.info(f"Generating embedding for document {mongo_id}")
        embedding = await embeddings_generator.fallback_embedding(cleaned_content)
        if not embedding:
            raise ValueError("Failed to generate embedding with both Hugging Face and Gemini")

        # Normalize the embedding
        embedding = embeddings_generator.normalize_embedding(embedding)
        logger.info(f"Generated normalized embedding for document {mongo_id}: {embedding[:5]}...")

        # Store in Qdrant
        point_id = str(mongo_id)
        payload = {
            "title": title,
            "content": cleaned_content,
            "processed_at": datetime.utcnow().isoformat(),
            "vector_source": "huggingface_with_gemini_fallback"
        }
        
        # Create collection if it doesn't exist
        collection_name = "documents"
        vector_size = len(embedding)
        if not qdrant_utils.create_collection(collection_name, vector_size):
            raise RuntimeError("Failed to create Qdrant collection")

        if not qdrant_utils.add_points(collection_name, [point_id], [embedding], [payload]):
            raise RuntimeError("Failed to add points to Qdrant")

        # Update MongoDB document with embedding and status
        process_time = (datetime.utcnow() - start_time).total_seconds()
        update_document(mongo_id, {
            "embedding": embedding,
            "status": "processed",
            "processed_at": datetime.utcnow(),
            "processing_time": process_time,
            "error_message": None,
            "vector_source": "huggingface_with_gemini_fallback"
        })

        logger.info(f"Successfully processed document {mongo_id} in {process_time:.2f} seconds")
        return True

    except ValueError as e:
        # Handle validation errors
        error_message = str(e)
        logger.warning(f"Validation error processing document {mongo_id}: {error_message}")
        update_document(mongo_id, {
            "status": "error",
            "error_message": error_message,
            "error_type": "validation_error",
            "error_at": datetime.utcnow()
        })
        return False
        
    except Exception as e:
        # Handle unexpected errors
        error_message = str(e)
        logger.error(f"Unexpected error processing document {mongo_id}: {error_message}", exc_info=True)
        update_document(mongo_id, {
            "status": "error",
            "error_message": error_message,
            "error_type": "system_error",
            "error_at": datetime.utcnow()
        })
        return False

async def reprocess_document(mongo_id: Union[str, ObjectId]) -> bool:
    """
    Reprocess a document that previously failed.
    
    Args:
        mongo_id: MongoDB document ID
    
    Returns:
        bool: True if reprocessing succeeded, False otherwise
    """
    try:
        doc = get_document(mongo_id)
        if not doc:
            logger.error(f"Document {mongo_id} not found")
            return False
        
        logger.info(f"Reprocessing document {mongo_id}")
        return await process_document(mongo_id, doc.get('title'), doc.get('content'))
    except Exception as e:
        logger.error(f"Error reprocessing document {mongo_id}: {e}", exc_info=True)
        return False
