import pytest
import main

@pytest.fixture
def client():
    main.app.testing = True
    yield main.app.test_client()

def test_one(client):
    assert client.get('/todos').status_code == 200
