from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.repositories.team_repository import TeamRepository
from fastapi import APIRouter, Depends, Request
from api_services.security.rate_limit import limiter

router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)

@router.get("/")
@limiter.limit("100/minute")
def get_teams(
    request: Request,
    db: Session = Depends(get_db)
):

    repository = TeamRepository(db)

    teams = repository.get_all()

    return [
        team.name
        for team in teams
    ]