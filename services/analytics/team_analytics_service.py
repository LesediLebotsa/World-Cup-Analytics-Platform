from services.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository

    def team_summary(self, team_name: str):

        team = self.repository.get_team(team_name)

        if team is None:
            raise ValueError("Team not found")

        matches = self.repository.matches_played(team.id)

        return {
            "team": team.name,
            "matches_played": matches
        }