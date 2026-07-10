import json
from api_services.cache.redis_client import redis_client

class CacheService:
    @staticmethod
    def get(key: str):

        value = redis_client.get(key)

        if value is None:
            return None

        return json.loads(value)

    @staticmethod
    def set(
            key: str,
            value,
            ttl: int = 86400
    ):

        redis_client.setex(
            key,
            ttl,
            json.dumps(value)
        )

    @staticmethod
    def delete(key: str):

        redis_client.delete(key)