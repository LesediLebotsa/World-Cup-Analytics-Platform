from sqlalchemy import select
from sqlalchemy.orm import Session
from services.models.team import Team

class TeamRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, team: Team) -> None:
        self.session.add(team)

    def get_by_name(self, name: str) -> Team | None:
        statement = select(Team).where(Team.name == name)
        return self.session.scalar(statement)

    def get_all(self) -> list[Team]:
        statement = select(Team)
        return list(self.session.scalars(statement))

    def get_team_lookup(self) -> dict[str, Team]:
        statement = select(Team)

        teams = self.session.scalars(statement)

        return {
            team.name: team
            for team in teams
        }