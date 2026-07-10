from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.exceptions import rate_limit_handler
from app.routers import (
    analytics,
    history,
    prediction,
    teams
)
from api_services.middleware.logging import LoggingMiddleware
from api_services.middleware.timing import TimingMiddleware
from api_services.security.rate_limit import limiter

app = FastAPI(
    title="World Cup Analytics & Prediction Platform",
)

# Middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(TimingMiddleware)
app.add_middleware(SlowAPIMiddleware)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    rate_limit_handler
)

# Routers
app.include_router(teams.router)
app.include_router(analytics.router)
app.include_router(prediction.router)
app.include_router(history.router)

# Root endpoint
@app.get("/")
def root():
    return {
        "application": "World Cup Analytics & Prediction Platform",
        "status": "online",
        "version": "1.1.0",
        "documentation": "/docs"
    }

# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }