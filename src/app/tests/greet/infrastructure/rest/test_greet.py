from app import create_app
import pytest

@pytest.fixture
def client():
    app, _ = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_greet(client):
    rv = client.get('/greet?name=John')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == 'Hello, John'

def test_greet_default(client):
    rv = client.get('/greet')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == 'Hello, World'
