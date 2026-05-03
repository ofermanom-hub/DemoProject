from src.auth.jwt import create_access_token, decode_access_token


def test_round_trip() -> None:
    token = create_access_token("user@example.com")
    sub = decode_access_token(token)
    assert sub == "user@example.com"
