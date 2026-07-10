from api_services.middleware.logging import LoggingMiddleware
from api_services.middleware.timing import TimingMiddleware
from fastapi import FastAPI
from app.routers import (
    analytics,
    history,
    prediction,
    teams
)

app = FastAPI(
    title="World Cup Analytics & Prediction Platform",
)

app.include_router(teams.router)
app.include_router(analytics.router)
app.include_router(prediction.router)
app.include_router(history.router)

app.add_middleware(LoggingMiddleware)
app.add_middleware(TimingMiddleware)

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }