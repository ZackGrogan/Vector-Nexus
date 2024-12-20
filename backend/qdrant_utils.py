import os
import logging
from typing import List, Dict, Optional, Any
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.exceptions import UnexpectedResponse
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

def get_qdrant_client() -> Optional[QdrantClient]:
    """
    Get a connection to Qdrant.
    
    Returns:
        Optional[QdrantClient]: Qdrant client if successful, None if failed
    """
    try:
        qdrant_url = os.getenv('QDRANT_URL', 'http://localhost:6333')
        return QdrantClient(url=qdrant_url)
    except Exception as e:
        logger.error(f"Failed to connect to Qdrant: {e}")
        return None

def create_collection(collection_name: str, vector_size: int) -> bool:
    """
    Create a collection in Qdrant if it doesn't exist.
    
    Args:
        collection_name: Name of the collection
        vector_size: Size of the vectors to store
        
    Returns:
        bool: True if collection exists or was created successfully, False otherwise
    """
    try:
        client = get_qdrant_client()
        if not client:
            return False

        # Check if collection exists
        collections = client.get_collections()
        if collection_name in [c.name for c in collections.collections]:
            return True

        # Create collection
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=models.Distance.COSINE
            )
        )
        
        logger.info(f"Created collection {collection_name}")
        return True

    except Exception as e:
        logger.error(f"Error creating collection: {e}")
        return False

def add_points(
    collection_name: str,
    ids: List[str],
    vectors: List[List[float]],
    payloads: List[Dict[str, Any]]
) -> bool:
    """
    Add points to a Qdrant collection.
    
    Args:
        collection_name: Name of the collection
        ids: List of point IDs
        vectors: List of vectors
        payloads: List of payloads
        
    Returns:
        bool: True if points were added successfully, False otherwise
    """
    try:
        client = get_qdrant_client()
        if not client:
            return False

        # Convert string IDs to integers using hash
        int_ids = [hash(id_) for id_ in ids]

        # Create points
        points = [
            models.PointStruct(
                id=id_,
                vector=vector,
                payload=payload
            )
            for id_, vector, payload in zip(int_ids, vectors, payloads)
        ]

        # Upsert points
        client.upsert(
            collection_name=collection_name,
            points=points
        )
        
        logger.info(f"Added {len(points)} points to collection {collection_name}")
        return True

    except Exception as e:
        logger.error(f"Error adding points: {e}")
        return False

def search_points(
    collection_name: str,
    vector: List[float],
    limit: int = 10,
    score_threshold: Optional[float] = None,
    filter_condition: Optional[Dict] = None
) -> Optional[Dict]:
    """
    Search for similar vectors in a Qdrant collection.
    
    Args:
        collection_name: Name of the collection
        vector: Query vector
        limit: Maximum number of results
        score_threshold: Minimum similarity score
        filter_condition: Filter condition for the search
        
    Returns:
        Optional[Dict]: Search results if successful, None if failed
    """
    try:
        client = get_qdrant_client()
        if not client:
            return None

        # Prepare search parameters
        search_params = {
            "collection_name": collection_name,
            "query_vector": vector,
            "limit": limit
        }

        # Add optional parameters
        if score_threshold is not None:
            search_params["score_threshold"] = score_threshold
        if filter_condition is not None:
            search_params["query_filter"] = models.Filter(**filter_condition)

        # Perform search
        results = client.search(**search_params)
        
        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                "id": result.id,
                "score": result.score,
                "payload": result.payload
            })

        return {
            "result": formatted_results,
            "total": len(formatted_results)
        }

    except UnexpectedResponse as e:
        if "not found" in str(e).lower():
            logger.warning(f"Collection {collection_name} not found")
            return {"result": [], "total": 0}
        logger.error(f"Unexpected response from Qdrant: {e}")
        return None
    except Exception as e:
        logger.error(f"Error searching points: {e}")
        return None

def delete_points(collection_name: str, ids: List[str]) -> bool:
    """
    Delete points from a Qdrant collection.
    
    Args:
        collection_name: Name of the collection
        ids: List of point IDs to delete
        
    Returns:
        bool: True if points were deleted successfully, False otherwise
    """
    try:
        client = get_qdrant_client()
        if not client:
            return False

        # Convert string IDs to integers using hash
        int_ids = [hash(id_) for id_ in ids]

        # Delete points
        client.delete(
            collection_name=collection_name,
            points_selector=models.PointIdsList(
                points=int_ids
            )
        )
        
        logger.info(f"Deleted {len(ids)} points from collection {collection_name}")
        return True

    except Exception as e:
        logger.error(f"Error deleting points: {e}")
        return False
