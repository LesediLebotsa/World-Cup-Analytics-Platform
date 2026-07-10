from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.repositories.analytics_repository import AnalyticsRepository
from services.prediction.explanation_service import ExplanationService
from services.prediction.prediction_engine import PredictionEngine
from fastapi import APIRouter, Depends, Request
from api_services.security.rate_limit import limiter

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.get("/")
@limiter.limit("30/minute")
def predict(
    request: Request,
    team1: str,
    team2: str,
    db: Session = Depends(get_db)
):

    repository = AnalyticsRepository(db)

    engine = PredictionEngine(repository)

    try:
        return engine.predict(team1, team2)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )