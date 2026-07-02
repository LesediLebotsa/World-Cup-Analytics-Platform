from services.config.prediction_config import RECENT_FORM_MATCHES
from services.config.tournament_categories import (WORLD_CUP,CONTINENTAL,QUALIFIER,REGIONAL)
from services.config.tournament_scoring import TOURNAMENT_SCORING
from services.repositories.analytics_repository import AnalyticsRepository
from config.prediction_config import MAX_POINTS

class TournamentImportanceService:
    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository

    def calculate(self, team_name: str):
        team = self.repository.get_team(team_name)

        if team is None:
            raise ValueError("Team not found")

        matches = self.repository.get_recent_matches(
            team.id,
            RECENT_FORM_MATCHES
        )

        weighted_points = 0

        for match in matches:
            category = self._get_category(match.tournament)

            is_home = match.home_team_id == team.id

            scored = match.home_goals if is_home else match.away_goals
            conceded = match.away_goals if is_home else match.home_goals

            if scored > conceded:
                result = "WIN"

            elif scored == conceded:
                result = "DRAW"

            else:
                result = "LOSS"

            weighted_points += self._match_points(
                category,
                result
            )

        importance_score = self._normalize_score(
            weighted_points,
            len(matches)
        )

        return {
            "team": team.name,
            "matches": len(matches),
            "weighted_points": weighted_points,
            "max_possible_points": len(matches) * 15,
            "importance_score": importance_score,
        }

    def _get_category(self, tournament: str) -> str:
        if tournament in WORLD_CUP:
            return "WORLD_CUP"

        if tournament in CONTINENTAL:
            return "CONTINENTAL"

        if tournament in QUALIFIER:
            return "QUALIFIER"

        if tournament in REGIONAL:
            return "REGIONAL"

        return "FRIENDLY"

    def _match_points(
        self,
        category: str,
        result: str
    ) -> int:

        return TOURNAMENT_SCORING[category][result]

    def _normalize_score(
        self,
        weighted_points: int,
        matches: int
    ) -> float:

        if matches == 0:
            return 0

        max_points = matches * 15

        return round(
            (weighted_points / max_points)
            * MAX_POINTS,
            2
        )