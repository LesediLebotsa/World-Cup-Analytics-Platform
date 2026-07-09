from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from services.history.world_cup_history_service import WorldCupHistoryService
from services.repositories.history_repository import HistoryRepository

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/overview")
def overview(
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.overview()

@router.get("/timeline")
def timeline(
        db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.timeline()

@router.get("/winners")
def winners(
        db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.winners()

@router.get("/tournament/{year}")
def tournament(
        year: int,
        db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.tournament(year)

@router.get("/facts")
def facts(
        db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.facts()