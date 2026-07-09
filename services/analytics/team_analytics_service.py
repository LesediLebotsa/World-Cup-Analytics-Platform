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
    def head_to_head(self,team_one_name: str,team_two_name: str):
        team_one = self.repository.get_team(team_one_name)
        team_two = self.repository.get_team(team_two_name)

        if team_one is None:
            raise ValueError(f"{team_one_name} not found")

        if team_two is None:
            raise ValueError(f"{team_two_name} not found")

        matches = self.repository.get_head_to_head_matches(
            team_one.id,
            team_two.id
        )

        team_one_wins = 0
        team_two_wins = 0
        draws = 0

        team_one_goals = 0
        team_two_goals = 0

        for match in matches:
            if match.home_team_id == team_one.id:

                team_one_goals += match.home_goals
                team_two_goals += match.away_goals

                if match.home_goals > match.away_goals:
                    team_one_wins += 1

                elif match.home_goals < match.away_goals:
                    team_two_wins += 1

                else:
                    draws += 1

            else:

                team_one_goals += match.away_goals
                team_two_goals += match.home_goals

                if match.away_goals > match.home_goals:
                    team_one_wins += 1

                elif match.away_goals < match.home_goals:
                    team_two_wins += 1

                else:
                    draws += 1

        total_matches = len(matches)

        return {
            "team_1": team_one.name,
            "team_2": team_two.name,

            "matches_played": total_matches,

            "team_1_wins": team_one_wins,
            "team_2_wins": team_two_wins,
            "draws": draws,

            "team_1_win_rate":
                round((team_one_wins / total_matches) * 100, 2)
                if total_matches else 0,

            "team_2_win_rate":
                round((team_two_wins / total_matches) * 100, 2)
                if total_matches else 0,

            "draw_rate":
                round((draws / total_matches) * 100, 2)
                if total_matches else 0,

            "team_1_goals": team_one_goals,
            "team_2_goals": team_two_goals,

            "goal_difference":
                team_one_goals - team_two_goals,

            "average_goals_per_match":
                round(
                    (team_one_goals + team_two_goals)
                    / total_matches,
                    2
                )
                if total_matches else 0
        }

    def recent_form(self, team_name:str, last_N:int = 10):
        team = self.repository.get_team(team_name)

        if team is None:
            raise ValueError("Team not found")

        matches = self.repository.get_recent_matches(team.id, last_N)

        wins = 0
        draws = 0
        losses = 0
        goals_scored = 0
        goals_conceded = 0
        points = 0

        form = []
        for match in matches:
            is_home = match.home_team_id == team.id

            scored = match.home_goals if is_home else match.away_goals
            conceded = match.away_goals if is_home else match.home_goals

            goals_scored += scored
            goals_conceded += conceded

            if scored > conceded:
                wins += 1
                points += 3
                form.append("W")
            elif scored == conceded:
                draws += 1
                points += 1
                form.append("D")
            else:
                losses += 1
                form.append("L")

        recent_form = "" .join(form)

        return {
            "team": team.name,
            "matches_played": len(matches),
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_scored": goals_scored,
            "goals_conceded": goals_conceded,
            "goal_difference": goals_scored - goals_conceded,
            "points": points,
            "form": recent_form,
            "win_rate(%)": round((wins / len(matches)) * 100, 2)
        }








