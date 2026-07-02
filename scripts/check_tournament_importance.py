from pprint import pprint
from services.analytics.tournament_importance_service import (TournamentImportanceService)
from services.config.database import SessionLocal
from services.repositories.analytics_repository import AnalyticsRepository

team_name = input("Team: ")

with SessionLocal() as session:
    repository = AnalyticsRepository(session)

    service = TournamentImportanceService(repository)

    pprint(
        service.calculate(team_name)
    )