from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.repositories.analytics_repository import AnalyticsRepository
from services.prediction.explanation_service import ExplanationService
from services.prediction.prediction_engine import PredictionEngine

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.get("/")
def predict(
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