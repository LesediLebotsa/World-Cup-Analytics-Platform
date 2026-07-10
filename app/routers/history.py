from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from services.history.world_cup_history_service import WorldCupHistoryService
from services.repositories.history_repository import HistoryRepository
from fastapi import APIRouter, Depends, Request
from api_services.security.rate_limit import limiter

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.get("/overview")
@limiter.limit("100/minute")
def overview(
    request: Request,
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.overview()

@router.get("/timeline")
@limiter.limit("100/minute")
def timeline(
    request: Request,
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.timeline()

@router.get("/winners")
@limiter.limit("100/minute")
def winners(
    request: Request,
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.winners()

@router.get("/tournament/{year}")
@limiter.limit("80/minute")
def tournament(
    request: Request,
    year: int,
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.tournament(year)

@router.get("/facts")
@limiter.limit("100/minute")
def facts(
    request: Request,
    db: Session = Depends(get_db)
):

    repository = HistoryRepository(db)
    service = WorldCupHistoryService(repository)

    return service.facts()