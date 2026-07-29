from fastapi.testclient import TestClient


def test_register_user_returns_created_user(client: TestClient) -> None:
    payload = {
        "email": "user@example.com",
        "username": "user",
        "password": "password123",
    }

    response = client.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 201
    assert response.json()["email"] == payload["email"]
    assert response.json()["username"] == payload["username"]
    assert "password" not in response.json()
    assert "hashed_password" not in response.json()
