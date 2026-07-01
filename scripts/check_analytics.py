from pprint import pprint
from services.repositories.analytics_repository import AnalyticsRepository
from services.analytics.team_analytics_service import TeamAnalyticsService
from services.config.database import SessionLocal


team_name = input("Enter team name: ")

with SessionLocal() as session:
    repository = AnalyticsRepository(session)

    analytics = TeamAnalyticsService(repository)

    pprint(
        analytics.team_summary(team_name)
    )