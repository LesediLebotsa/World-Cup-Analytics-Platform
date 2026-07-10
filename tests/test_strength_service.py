from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_compare():

    response = client.get(
        "/analytics/compare",
        params={
            "team1": "Brazil",
            "team2": "Germany"
        }
    )

    assert response.status_code == 200

    comparison = response.json()

    assert "team_one" in comparison

    assert "team_two" in comparison

    assert "head_to_head" in comparison