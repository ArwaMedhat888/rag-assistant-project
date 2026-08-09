from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_query_success():
    response = client.post(
        "/query",
        json={"question": "What is deep learning?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "question" in data
    assert "answer" in data
    assert "sources" in data

    assert data["question"] == "What is deep learning?"
    assert isinstance(data["answer"], str)
    assert isinstance(data["sources"], list)