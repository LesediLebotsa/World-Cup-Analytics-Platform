from services.repositories.analytics_repository import AnalyticsRepository


class TeamAnalyticsService:

    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository

    def team_summary(self, team_name: str):

        team = self.repository.get_team(team_name)

        if team is None:
            raise ValueError("Team not found")

        matches = self.repository.get_matches(team.id)

        wins = 0
        draws = 0
        goals_scored = 0
        goals_conceded = 0

        for match in matches:

            is_home = match.home_team_id == team.id

            scored = match.home_goals if is_home else match.away_goals
            conceded = match.away_goals if is_home else match.home_goals

            goals_scored += scored
            goals_conceded += conceded

            if scored > conceded:
                wins += 1
            elif scored == conceded:
                draws += 1

        matches_played = len(matches)
        losses = matches_played - wins - draws

        win_percentage = (
            round((wins / matches_played) * 100, 2)
            if matches_played
            else 0
        )

        return {
            "team": team.name,
            "matches_played": matches_played,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_scored": goals_scored,
            "goals_conceded": goals_conceded,
            "goal_difference": goals_scored - goals_conceded,
            "win_percentage": win_percentage,
        }