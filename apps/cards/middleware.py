import logging
import time

logger = logging.getLogger(__name__)

class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.get_full_path()}")

        response = self.get_response(request)

        duration = time.time() - start_time
        logger.info(f"Response: {response.status_code} {response.reason_phrase} ({duration:.2f} seconds)")

        return response
