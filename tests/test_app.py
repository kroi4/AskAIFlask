import pytest
from flask.testing import FlaskClient
from app import create_app
from typing import Generator

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_text(client: FlaskClient):
    response = client.post('/ask', json={'prompt': 'What is the capital of France?'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data
    assert 'Paris' in data['response']