from services.repositories.match_repository import MatchRepository
from services.repositories.team_repository import TeamRepository


class TeamAnalyticsService:

    def __init__(
        self,
        team_repository: TeamRepository,
        match_repository: MatchRepository,
    ):
        self.team_repository = team_repository
        self.match_repository = match_repository

    def summary(self, team_name: str):

        team = self.team_repository.get_by_name(team_name)

        if team is None:
            raise ValueError("Team not found")

        matches = self.match_repository.get_matches_for_team(team.id)

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

        losses = len(matches) - wins - draws

        return {
            "team": team.name,
            "matches_played": len(matches),
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_scored": goals_scored,
            "goals_conceded": goals_conceded,
            "goal_difference": goals_scored - goals_conceded,
            "win_percentage": round(
                (wins / len(matches)) * 100, 2
            ) if matches else 0
        }