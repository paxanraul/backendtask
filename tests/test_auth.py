import pytest


@pytest.fixture
def register_data():
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@test.com",
        "password": "testpassword123"
    }


def test_register_success(client, register_data):
    response = client.post("/auth/register", json=register_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@test.com"
    assert "password" not in data


def test_register_duplicate_email(client, register_data):
    client.post("/auth/register", json=register_data)
    response = client.post("/auth/register", json=register_data)
    assert response.status_code == 400


def test_login_success(client, register_data):
    client.post("/auth/register", json=register_data)
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "testpassword123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login_wrong_password(client, register_data):
    client.post("/auth/register", json=register_data)
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401


def test_logout_success(client, register_data):
    client.post("/auth/register", json=register_data)
    login = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "testpassword123"
    })
    token = login.json()["access_token"]
    response = client.post(
        "/auth/logout",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200