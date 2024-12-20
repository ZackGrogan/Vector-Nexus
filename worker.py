import os
from rq import Worker, Queue, Connection
from backend.redis_utils import get_redis_connection

if __name__ == '__main__':
    redis_conn = get_redis_connection()
    with Connection(redis_conn):
        worker = Worker(['vector_nexus'])
        worker.work()
