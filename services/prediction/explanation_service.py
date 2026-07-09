class ExplanationService:

    def generate(
        self,
        team_one_strength: dict,
        team_two_strength: dict,
        head_to_head: dict,
        difference: float
    ):

        explanations = []

        team_one = team_one_strength["team"]
        team_two = team_two_strength["team"]

        summary_one = team_one_strength["team_summary"]
        summary_two = team_two_strength["team_summary"]

        recent_one = team_one_strength["recent_form_summary"]
        recent_two = team_two_strength["recent_form_summary"]

        # Recent Form
        explanations.append({
            "category": "Recent Form",
            "message":
                f"{team_one} won {recent_one['wins']} of their last "
                f"{recent_one['matches_played']} matches, while "
                f"{team_two} won {recent_two['wins']}."
        })

        # Historical Record
        explanations.append({
            "category": "Historical Record",
            "message":
                f"{team_one} has a historical win percentage of "
                f"{summary_one['win_percentage']}%, compared to "
                f"{summary_two['win_percentage']}% for {team_two}."
        })

        # Goal Difference
        explanations.append({
            "category": "Goal Difference",
            "message":
                f"{team_one} has a goal difference of "
                f"{summary_one['goal_difference']}, while "
                f"{team_two} has "
                f"{summary_two['goal_difference']}."
        })

        # Head-to-head
        if head_to_head["matches_played"] > 0:

            explanations.append({

                "category": "Head-to-Head",

                "message":
                    f"The teams have met "
                    f"{head_to_head['matches_played']} times. "
                    f"{team_one} has won "
                    f"{head_to_head['team_1_wins']}, "
                    f"{team_two} has won "
                    f"{head_to_head['team_2_wins']}, "
                    f"with {head_to_head['draws']} draws."

            })

        # Prediction
        winner = (
            team_one
            if team_one_strength["strength_score"] >
               team_two_strength["strength_score"]
            else team_two
        )

        explanations.append({

            "category": "Prediction",

            "message":
                f"{winner} is predicted to win because their "
                f"overall strength score is higher. "
                f"The final difference between the teams is "
                f"{difference:.2f} points."

        })

        return explanations

    def _compare_component(
            self,
            explanations,
            category,
            component,
            team_one,
            team_two,
            team_one_components,
            team_two_components,
            message,
    ):

        first = team_one_components[component]
        second = team_two_components[component]

        if first > second:
            explanations.append({
                "category": category,
                "winner": team_one,
                "message": (
                    f"{team_one} outperformed {team_two} in {category.lower()} "
                    f"({first:.2f} vs {second:.2f}), indicating {message}."
                )
            })

        elif second > first:
            explanations.append({
                "category": category,
                "winner": team_two,
                "message": (
                    f"{team_two} outperformed {team_one} in {category.lower()} "
                    f"({second:.2f} vs {first:.2f}), indicating {message}."
                )
            })

        else:
            explanations.append({
                "category": category,
                "winner": None,
                "message": (
                    f"Both teams recorded identical {category.lower()} scores "
                    f"({first:.2f})."
                )
            })