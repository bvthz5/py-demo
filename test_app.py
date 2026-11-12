
from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    # Check HTTP status
    assert response.status_code == 200

    # Strictly compare the complete response
    assert response.data == b"hi CI/CD Pipeline!"