from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from services.models.match import Match


class MatchRepository:

    def __init__(self, session: Session):
        self.session = session

    def add(self, match: Match) -> None:
        self.session.add(match)

    def get_all(self) -> list[Match]:
        statement = select(Match)
        return list(self.session.scalars(statement))

    def get_matches_for_team(self, team_id: int) -> list[Match]:
        statement = (
            select(Match)
            .where(
                or_(
                    Match.home_team_id == team_id,
                    Match.away_team_id == team_id
                )
            )
        )

        return list(self.session.scalars(statement))