from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_teams():

    response = client.get("/teams")

    assert response.status_code == 200

    teams = response.json()

    assert isinstance(teams, list)

    assert len(teams) > 0

    assert "South Africa" in teams