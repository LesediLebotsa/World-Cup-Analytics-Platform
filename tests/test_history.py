from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_history_overview():

    response = client.get("/history/overview")

    assert response.status_code == 200

    overview = response.json()

    assert overview["first_world_cup"] == 1930
    assert overview["latest_world_cup"] == 2018
    assert overview["different_champions"] >= 8
    assert overview["average_goals_per_tournament"] > 0

def test_history_timeline():

    response = client.get("/history/timeline")

    assert response.status_code == 200

    timeline = response.json()

    assert isinstance(timeline, list)

    assert len(timeline) > 0

def test_history_winners():

    response = client.get("/history/winners")

    assert response.status_code == 200

    winners = response.json()

    assert isinstance(winners, list)

    assert len(winners) > 0

def test_history_tournament():

    response = client.get("/history/tournament/2018")

    assert response.status_code == 200

    tournament = response.json()

    assert tournament["year"] == 2018

def test_history_facts():

    response = client.get("/history/facts")

    assert response.status_code == 200

    facts = response.json()

    assert isinstance(facts, dict)