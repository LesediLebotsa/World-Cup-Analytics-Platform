import os
import redis

redis_client = None

redis_url = os.getenv("REDIS_URL")

if redis_url:
    try:
        redis_client = redis.from_url(
            redis_url,
            decode_responses=True
        )
        redis_client.ping()
    except Exception:
        redis_client = None