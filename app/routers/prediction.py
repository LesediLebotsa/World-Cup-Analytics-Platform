from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.repositories.analytics_repository import AnalyticsRepository
from services.analytics.strength_score_services import StrengthScoreService
from services.analytics.team_analytics_service import TeamAnalyticsService
from services.analytics.tournament_importance_service import TournamentImportanceService
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

    analytics = TeamAnalyticsService(repository)
    strength = StrengthScoreService(repository)
    tournament = TournamentImportanceService(repository)
    explanation = ExplanationService()

    engine = PredictionEngine(
        analytics,
        strength,
        tournament,
        explanation
    )

    try:
        return engine.predict(team1, team2)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )