from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_word_frequency_endpoint_basic():
    response = client.get("/word-frequency", params={"article": "Python", "depth": 0})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_keywords_endpoint_basic():
    payload = {
        "article": "Python",
        "depth": 0,
        "ignore_list": ["python"],
        "percentile": 50,
    }
    response = client.post("/keywords", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
