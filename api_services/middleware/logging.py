import logging
import sys
import time
from starlette.middleware.base import BaseHTTPMiddleware


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        logging.info(
            "%s %s %s %.3fs",
            request.method,
            request.url.path,
            response.status_code,
            duration
        )

        return response