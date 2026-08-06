import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.mark.parametrize("path, expected_status", [("/", 307), ("/activities", 200)])
def test_pytest_smoke_routes(path, expected_status):
    client = TestClient(app)
    response = client.get(path, follow_redirects=False)

    assert response.status_code == expected_status
    if path == "/":
        assert response.headers["location"] == "/static/index.html"
