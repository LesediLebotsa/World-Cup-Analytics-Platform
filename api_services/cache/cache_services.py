import json
from api_services.cache.redis_client import redis_client

class CacheService:

    @staticmethod
    def get(key):

        if redis_client is None:
            return None

        value = redis_client.get(key)

        if value is None:
            return None

        return json.loads(value)

    @staticmethod
    def set(key, value, ttl=86400):

        if redis_client is None:
            return

        redis_client.setex(
            key,
            ttl,
            json.dumps(value)
        )