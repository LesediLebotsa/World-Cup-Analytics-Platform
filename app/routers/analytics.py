from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.analytics.strength_score_services import StrengthScoreService
from app.dependencies import get_db
from services.repositories.analytics_repository import AnalyticsRepository
from services.analytics.team_analytics_service import TeamAnalyticsService
from fastapi import APIRouter, Depends, Request
from api_services.security.rate_limit import limiter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/summary/{team_name}")
@limiter.limit("100/minute")
def team_summary(
    request: Request,
    team_name: str,
    db: Session = Depends(get_db)
):
    repository = AnalyticsRepository(db)
    service = TeamAnalyticsService(repository)

    try:
        return service.team_summary(team_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get("/recent-form/{team_name}")
@limiter.limit("100/minute")
def recent_form(
    request: Request,
    team_name: str,
    db: Session = Depends(get_db)
):

    repository = AnalyticsRepository(db)
    service = TeamAnalyticsService(repository)

    try:
        return service.recent_form(team_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get("/head-to-head")
@limiter.limit("100/minute")
def head_to_head(
    request: Request,
    team1: str,
    team2: str,
    db: Session = Depends(get_db)
):
    repository = AnalyticsRepository(db)
    service = TeamAnalyticsService(repository)

    try:
        return service.head_to_head(
            team1,
            team2
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get("/strength/{team_name}")
def strength_score(
    team_name: str,
    db: Session = Depends(get_db)
):
    repository = AnalyticsRepository(db)
    service = StrengthScoreService(repository)

    try:
        return service.calculate(team_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get("/compare")
def compare_teams(
    team1: str,
    team2: str,
    db: Session = Depends(get_db)
):
    repository = AnalyticsRepository(db)

    analytics = TeamAnalyticsService(repository)
    strength = StrengthScoreService(repository)

    return {
        "team_one": {
            **analytics.team_summary(team1),
            "strength_score": strength.calculate(team1)["strength_score"]
        },
        "team_two": {
            **analytics.team_summary(team2),
            "strength_score": strength.calculate(team2)["strength_score"]
        },
        "head_to_head": analytics.head_to_head(
            team1,
            team2
        )
    }