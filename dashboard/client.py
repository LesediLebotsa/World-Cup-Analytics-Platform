import requests
from config import BASE_URL

class APIClient:

    def get_teams(self):
        response = requests.get(
            f"{BASE_URL}/teams"
        )
        response.raise_for_status()
        return response.json()

    def team_summary(self, team):
        response = requests.get(
            f"{BASE_URL}/analytics/team/{team}"
        )
        response.raise_for_status()
        return response.json()

    def recent_form(self, team):
        response = requests.get(
            f"{BASE_URL}/analytics/recent-form/{team}"
        )
        response.raise_for_status()
        return response.json()

    def head_to_head(self, team1, team2):
        response = requests.get(
            f"{BASE_URL}/analytics/head-to-head",
            params={
                "team1": team1,
                "team2": team2
            }
        )
        response.raise_for_status()
        return response.json()

    def strength(self, team):
        response = requests.get(
            f"{BASE_URL}/analytics/strength/{team}"
        )
        response.raise_for_status()
        return response.json()

    def prediction(self, team1, team2):
        response = requests.get(
            f"{BASE_URL}/prediction",
            params={
                "team1": team1,
                "team2": team2
            }
        )
        response.raise_for_status()
        return response.json()

    def compare(
            self,
            team1,
            team2
    ):
        response = requests.get(
            f"{BASE_URL}/analytics/compare",
            params={
                "team1": team1,
                "team2": team2
            }
        )

        response.raise_for_status()

        return response.json()

    def history_overview(self):
        response = requests.get(
            f"{BASE_URL}/history/overview"
        )
        response.raise_for_status()
        return response.json()

    def history_timeline(self):
        response = requests.get(
            f"{BASE_URL}/history/timeline"
        )
        response.raise_for_status()
        return response.json()

    def history_winners(self):
        response = requests.get(
            f"{BASE_URL}/history/winners"
        )
        response.raise_for_status()
        return response.json()

    def history_facts(self):
        response = requests.get(
            f"{BASE_URL}/history/facts"
        )
        response.raise_for_status()
        return response.json()

    def tournament(self, year):
        response = requests.get(
            f"{BASE_URL}/history/tournament/{year}"
        )
        response.raise_for_status()
        return response.json()