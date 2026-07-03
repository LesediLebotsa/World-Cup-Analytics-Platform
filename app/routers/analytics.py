from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from services.repositories.analytics_repository import AnalyticsRepository
from services.analytics.team_analytics_service import TeamAnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/team/{team_name}")
def team_summary(
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
def recent_form(
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

@router.get("/recent-form/{team_name}")
def recent_form(
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
def head_to_head(
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