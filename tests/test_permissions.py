import pytest 


@pytest.fixture
def user_client(client):
    client.post("/auth/register", json={
        "first_name": "Test",
        "last_name": "User",
        "email": "user@test.com",
        "password": "testpassword123"
    })
    login = client.post("/auth/login", json={
        "email": "user@test.com",
        "password": "testpassword123"
    })
    token = login.json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client


def test_user_can_read_products(user_client):
    response = user_client.get("/mock/products/my")
    assert response.status_code == 200


def test_user_cannot_create_products(user_client):
    response = user_client.post("/mock/products")
    assert response.status_code == 403


def test_user_cannot_read_all_orders(user_client):
    response = user_client.get("/mock/orders/all")
    assert response.status_code == 403


def test_user_can_read_own_orders(user_client):
    response = user_client.get("/mock/orders")
    assert response.status_code == 200


def test_unauthorized_cannot_access_mock(client):
    response = client.get("/mock/products/my")
    assert response.status_code == 401