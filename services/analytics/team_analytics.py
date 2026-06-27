from services.analytics.team_analytics_service import AnalyticsService
from services.config.database import SessionLocal
from services.repositories.analytics_repository import AnalyticsRepository

with SessionLocal() as session:

    repository = AnalyticsRepository(session)

    analytics = AnalyticsService(repository)

    print(
        analytics.team_summary("Argentina")
    )