import pytest


@pytest.fixture
def auth_client(client):
    client.post("/auth/register", json={
        "first_name": "Test",
        "last_name": "User",
        "email": "test@test.com",
        "password": "testpassword123",
        "password_confirm": "testpassword123"
    })
    login = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "testpassword123"
    })
    token = login.json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client


def test_get_me_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401
    data = response.json()


def test_get_me_success(auth_client):
    response = auth_client.get("/users/me")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@test.com"


def test_update_me(auth_client):
    response = auth_client.patch("/users/me", json={
        "first_name": "Updated"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Updated"


def test_delete_me(auth_client):
    response = auth_client.delete("/users/me")
    assert response.status_code == 204
    response = auth_client.get("/users/me")
    assert response.status_code == 401