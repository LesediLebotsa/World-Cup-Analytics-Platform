from fastapi import FastAPI
from app.routers import (
    health,
    teams,
    analytics,
    prediction,
)

app = FastAPI(
    title="World Cup Analytics & Prediction API",
    description="REST API for football analytics and World Cup match predictions.",
    version="1.0.0",
)
@app.get("/", tags=["Root"])
def root():
    return {
        "name": "World Cup Analytics & Prediction API",
        "version": "1.0.0",
        "documentation": "/docs",
        "health": "/health",
    }
app.include_router(health.router)
app.include_router(teams.router)
app.include_router(analytics.router)
app.include_router(prediction.router)