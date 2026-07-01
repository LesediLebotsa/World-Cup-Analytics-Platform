from pprint import pprint
from services.repositories.analytics_repository import AnalyticsRepository
from services.analytics.team_analytics_service import TeamAnalyticsService
from services.config.database import SessionLocal


# team_name = input("Enter team name: ")

with SessionLocal() as session:
    repository = AnalyticsRepository(session)

    team_one = input("Team 1: ")
    team_two = input("Team 2: ")

    analytics = TeamAnalyticsService(repository)

    pprint(
        analytics.head_to_head(team_one, team_two)
    )


