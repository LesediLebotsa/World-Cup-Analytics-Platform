from services.analytics.team_analytics_service import TeamAnalyticsService
from services.repositories.analytics_repository import AnalyticsRepository
from services.config.prediction_config import (
    MAX_STRENGTH_SCORE,
    RECENT_FORM_WEIGHT,
    WIN_PERCENTAGE_WEIGHT,
    GOAL_DIFFERENCE_WEIGHT,
)

class StrengthScoreService:
    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository
        self.analytics = TeamAnalyticsService(repository)

    def calculate(self, team_name: str):
        summary = self.analytics.team_summary(team_name)
        recent = self.analytics.recent_form(team_name)

        recent_form_score = self._recent_form_score(recent)
        win_percentage_score = self._win_percentage_score(summary)
        goal_difference_score = self._goal_difference_score(recent)

        raw_score = (
            recent_form_score
            + win_percentage_score
            + goal_difference_score
        )

        strength_score = round(
            (raw_score / MAX_STRENGTH_SCORE) * 100,
            2
        )

        return {
            "team": team_name,
            "strength_score": strength_score,
            "components": {
                "recent_form": recent_form_score,
                "win_percentage": win_percentage_score,
                "goal_difference": goal_difference_score
            },
            "team_summary": summary,
            "recent_form_summary": recent
        }

    def _recent_form_score(self, recent: dict) -> float:
        matches = recent["matches_played"]

        if matches == 0:
            return 0

        return round(
            (recent["points"] / (matches * 3))
            * RECENT_FORM_WEIGHT,
            2
        )

    def _win_percentage_score(self, summary: dict) -> float:
        return round(
            (summary["win_percentage"] / 100)
            * WIN_PERCENTAGE_WEIGHT,
            2
        )

    def _goal_difference_score(self, recent: dict) -> float:
        matches = recent["matches_played"]

        if matches == 0:
            return 0

        average_goal_difference = (
            recent["goal_difference"] / matches
        )

        normalized = min(
            max((average_goal_difference + 3) / 6, 0),
            1
        )

        return round(
            normalized * GOAL_DIFFERENCE_WEIGHT,
            2
        )