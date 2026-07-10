from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_team_summary():

    response = client.get(
        "/analytics/team/South Africa"
    )

    assert response.status_code == 200

    summary = response.json()

    assert summary["team"] == "South Africa"

    assert summary["matches_played"] >= 0

    assert summary["wins"] >= 0

    assert summary["draws"] >= 0

    assert summary["losses"] >= 0

def test_recent_form():

    response = client.get(
        "/analytics/recent-form/South Africa"
    )

    assert response.status_code == 200

    recent = response.json()

    assert recent["team"] == "South Africa"

    assert recent["matches_played"] <= 10

def test_head_to_head():

    response = client.get(
        "/analytics/head-to-head",
        params={
            "team1": "Brazil",
            "team2": "Argentina"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["team_1"] == "Brazil"

    assert data["team_2"] == "Argentina"

def test_invalid_team():

    response = client.get(
        "/analytics/team/ABCXYZ"
    )

    assert response.status_code == 404