from services.analytics.strength_score_services import StrengthScoreService
from services.analytics.team_analytics_service import TeamAnalyticsService
from services.repositories.analytics_repository import AnalyticsRepository
from services.config.prediction_config import (DRAW_THRESHOLD,SLIGHT_FAVOURITE_THRESHOLD,FAVOURITE_THRESHOLD,
                                               HEAD_TO_HEAD_CLOSE_GAME_THRESHOLD,HEAD_TO_HEAD_MIN_MATCHES,
                                               HEAD_TO_HEAD_BONUS)
from services.prediction.explanation_service import ExplanationService

class PredictionEngine:
    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository
        self.strength = StrengthScoreService(repository)
        self.analytics = TeamAnalyticsService(repository)
        self.explanation =  ExplanationService()

    def predict(
            self,
            team_one: str,
            team_two: str
    ):

        # Calculate strength scores
        team_one_strength = self.strength.calculate(team_one)
        team_two_strength = self.strength.calculate(team_two)

        # Retrieve head-to-head statistics
        head_to_head = self.analytics.head_to_head(
            team_one,
            team_two
        )

        # Apply head-to-head bonus (if applicable)
        team_one_score, team_two_score = (
            self._apply_head_to_head_bonus(
                team_one_strength["strength_score"],
                team_two_strength["strength_score"],
                head_to_head
            )
        )

        # Calculate score difference
        difference = abs(
            team_one_score - team_two_score
        )

        # Determine winner
        winner = self._determine_winner(
            team_one,
            team_two,
            team_one_score,
            team_two_score
        )

        # Determine confidence
        confidence = self._determine_confidence(
            difference
        )

        # Generate explanation
        explanation = self.explanation.generate(
            team_one_strength,
            team_two_strength,
            difference
        )

        return {
            "team_1": team_one,
            "team_2": team_two,

            "team_1_strength": round(team_one_score, 2),
            "team_2_strength": round(team_two_score, 2),

            "difference": round(difference, 2),

            "prediction": winner,

            "confidence": confidence,

            "head_to_head": head_to_head,

            "explanation": explanation
        }

    def _determine_winner(
            self,
            team_one: str,
            team_two: str,
            team_one_score: float,
            team_two_score: float
    ):

        if team_one_score > team_two_score:
            return team_one

        elif team_two_score > team_one_score:
            return team_two

        return "Draw"

    def _determine_confidence(
        self,
        difference: float
    ) -> str:

        if difference <= DRAW_THRESHOLD:
            return "Too Close To Call"

        if difference <= SLIGHT_FAVOURITE_THRESHOLD:
            return "Slight Favourite"

        if difference <= FAVOURITE_THRESHOLD:
            return "Favourite"

        return "Heavy Favourite"

    def _apply_head_to_head_bonus(
            self,
            team_one_score,
            team_two_score,
            head_to_head
    ):
        matches = head_to_head["matches_played"]

        if matches < HEAD_TO_HEAD_MIN_MATCHES:
            return team_one_score, team_two_score

        difference = abs(team_one_score - team_two_score)

        if difference > HEAD_TO_HEAD_CLOSE_GAME_THRESHOLD:
            return team_one_score, team_two_score

        if head_to_head["team_1_wins"] > head_to_head["team_2_wins"]:
            team_one_score += HEAD_TO_HEAD_BONUS

        elif head_to_head["team_2_wins"] > head_to_head["team_1_wins"]:
            team_two_score += HEAD_TO_HEAD_BONUS

        return team_one_score, team_two_score