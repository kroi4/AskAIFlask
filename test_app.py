import pytest
from flask import Flask
from flask.testing import FlaskClient
import json
from app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_text(client: FlaskClient):
    response = client.post('/ask', json={'prompt': 'What is the capital of France?'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'response' in data
    assert 'Paris' in data['response']
