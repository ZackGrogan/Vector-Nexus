import os
from typing import Optional
import redis
from rq import Queue
import logging

logger = logging.getLogger(__name__)

def get_redis_connection() -> Optional[redis.Redis]:
    """
    Get a connection to Redis.
    
    Returns:
        Optional[redis.Redis]: Redis connection if successful, None if failed
    """
    try:
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        
        return redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=True
        )
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {e}")
        return None

def get_task_queue() -> Optional[Queue]:
    """
    Get the RQ task queue.
    
    Returns:
        Optional[Queue]: RQ queue if Redis connection successful, None if failed
    """
    try:
        redis_conn = get_redis_connection()
        if redis_conn:
            return Queue('vector_nexus', connection=redis_conn)
        return None
    except Exception as e:
        logger.error(f"Failed to create task queue: {e}")
        return None
