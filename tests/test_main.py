"""
Module for functional test cases of main script.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

'''
def test_server_status():
    """Tests if server is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API server is running"}


def test_model_output():
    """Tests if output generation api is up and giving expected result."""
    response = client.post(
        "/news_articles/", json={"query": "Tesla", "num_articles": 2}
    )
    assert response.status_code == 200
'''
