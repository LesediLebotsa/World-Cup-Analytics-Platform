from sqlalchemy import or_, func, select
from sqlalchemy.orm import Session

from services.models.match import Match
from services.models.team import Team


class AnalyticsRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_team(self, name: str) -> Team | None:
        statement = select(Team).where(
            Team.name == name
        )
        return self.session.scalar(statement)

    def matches_played(self, team_id: int) -> int:
        statement = (
            select(func.count())
            .select_from(Match)
            .where(
                (Match.home_team_id == team_id)
                | (Match.away_team_id == team_id)
            )
        )
        return self.session.scalar(statement)

    def get_matches(self, team_id: int) -> list[Match]:
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