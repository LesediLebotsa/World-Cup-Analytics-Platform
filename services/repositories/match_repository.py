from sqlalchemy.orm import Session
from sqlalchemy import select
from services.models.match import Match

class MatchRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, match: Match) -> None:
        self.session.add(match)

    def get_all(self) -> list[Match]:
        statement = select(Match)
        return list(self.session.scalars(statement))