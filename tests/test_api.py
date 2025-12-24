import json
from api.app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert "status" in response.get_json()


def test_predict_endpoint():
    client = app.test_client()

    payload = {
        "country": "United Kingdom",
        "date": "2019-02-01"
    }

    response = client.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200

    data = response.get_json()
    assert "predicted_revenue" in data
    assert data["country"] == "United Kingdom"
