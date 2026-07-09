from sqlalchemy.orm import Session
from services.models.world_cup import WorldCup
from services.models.match import Match
from collections import Counter

class HistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_world_cups(self):
        return (
            self.db.query(WorldCup)
            .order_by(WorldCup.year)
            .all()
        )

    def total_matches(self):
        return self.db.query(Match).count()

    def total_goals(self):
        matches = self.db.query(Match).all()

        return sum(
            match.home_goals + match.away_goals
            for match in matches
        )

    def winner_counts(self):
        tournaments = self.get_world_cups()

        return Counter(
            tournament.winner
            for tournament in tournaments
        )

    def highest_scoring_world_cup(self):
        return (
            self.db.query(WorldCup)
            .order_by(WorldCup.goals_scored.desc())
            .first()
        )

    def first_world_cup(self):
        return (
            self.db.query(WorldCup)
            .order_by(WorldCup.year)
            .first()
        )

    def latest_world_cup(self):
        return (
            self.db.query(WorldCup)
            .order_by(WorldCup.year.desc())
            .first()
        )

    def tournament_by_year(
            self,
            year: int
    ):
        return (
            self.db.query(WorldCup)
            .filter(WorldCup.year == year)
            .first()
        )