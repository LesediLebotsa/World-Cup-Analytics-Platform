from pprint import pprint

from services.config.database import SessionLocal
from services.repositories.analytics_repository import AnalyticsRepository
from services.prediction.prediction_engine import PredictionEngine

team_one = input("Team 1: ")
team_two = input("Team 2: ")

with SessionLocal() as session:

    repository = AnalyticsRepository(session)

    engine = PredictionEngine(repository)

    pprint(
        engine.predict(team_one, team_two)
    )