from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.repositories.team_repository import TeamRepository

router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)

@router.get("/")
def get_teams(
    db: Session = Depends(get_db)
):

    repository = TeamRepository(db)

    teams = repository.get_all()

    return [
        team.name
        for team in teams
    ]