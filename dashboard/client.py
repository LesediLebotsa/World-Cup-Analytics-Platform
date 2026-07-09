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