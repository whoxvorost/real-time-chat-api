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


def test_register_user_with_existing_email_returns_bad_request(
    client: TestClient,
) -> None:
    payload = {
        "email": "user@example.com",
        "username": "user",
        "password": "password123",
    }

    client.post("/api/v1/auth/register", json=payload)

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": payload["email"],
            "username": "another_user",
            "password": "password123",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_register_user_with_existing_username_returns_bad_request(
    client: TestClient,
) -> None:
    payload = {
        "email": "user@example.com",
        "username": "user",
        "password": "password123",
    }

    client.post("/api/v1/auth/register", json=payload)

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "another@example.com",
            "username": payload["username"],
            "password": "password123",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"
