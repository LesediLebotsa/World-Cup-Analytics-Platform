from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_prediction():

    response = client.get(
        "/prediction",
        params={
            "team1": "Brazil",
            "team2": "Argentina"
        }
    )

    assert response.status_code == 200

    prediction = response.json()

    assert "prediction" in prediction

    assert "confidence" in prediction

    assert "difference" in prediction

def test_invalid_prediction():

    response = client.get(
        "/prediction",
        params={
            "team1": "ABC",
            "team2": "XYZ"
        }
    )

    assert response.status_code == 404