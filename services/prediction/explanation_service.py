class ExplanationService:
    def generate(
        self,
        team_one_strength: dict,
        team_two_strength: dict,
        difference: float
    ):

        explanations = []

        team_one = team_one_strength["team"]
        team_two = team_two_strength["team"]

        team_one_components = team_one_strength["components"]
        team_two_components = team_two_strength["components"]

        self._compare_component(
            explanations,
            "Recent Form",
            "recent_form",
            team_one,
            team_two,
            team_one_components,
            team_two_components,
            "stronger recent form"
        )

        self._compare_component(
            explanations,
            "Win Percentage",
            "win_percentage",
            team_one,
            team_two,
            team_one_components,
            team_two_components,
            "a higher historical win percentage"
        )

        self._compare_component(
            explanations,
            "Goal Difference",
            "goal_difference",
            team_one,
            team_two,
            team_one_components,
            team_two_components,
            "a better recent goal difference"
        )

        explanations.append({
            "category": "Overall",
            "winner": None,
            "message": (
                f"The overall strength score difference is "
                f"{round(difference, 2)} points."
            )
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
        message
    ):

        first = team_one_components[component]
        second = team_two_components[component]

        if first > second:
            explanations.append({
                "category": category,
                "winner": team_one,
                "message": f"{team_one} has {message}."
            })

        elif second > first:
            explanations.append({
                "category": category,
                "winner": team_two,
                "message": f"{team_two} has {message}."
            })

        else:
            explanations.append({
                "category": category,
                "winner": None,
                "message": f"Both teams are evenly matched for {category.lower()}."
            })