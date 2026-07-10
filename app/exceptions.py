from fastapi.responses import JSONResponse

def rate_limit_handler(request, exc):

    return JSONResponse(
        status_code=429,
        content={
            "error": "Too Many Requests",
            "message": "Rate limit exceeded. Please try again later."
        }
    )