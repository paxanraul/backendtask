from app.core.security import hash_password, verify_password, create_access_token, decode_access_token


def test_hash_password():
    hashed = hash_password("mypassword")
    assert hashed != "mypassword"


def test_verify_password_correct():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed) == True


def test_verify_password_wrong():
    hashed = hash_password("mypassword")
    assert verify_password("wrongpassword", hashed) == False


def test_create_and_decode_token():
    token = create_access_token({"sub": "123"})
    payload = decode_access_token(token)
    assert payload["sub"] == "123"


def test_decode_invalid_token():
    payload = decode_access_token("invalid.token.here")
    assert payload is None