import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_rendering(client):
    """Verifies that the home page renders the Bootstrap navbar"""
    response = client.get('/')
    assert b'Student Portal' in response.data
    assert response.status_code == 200

def test_api_status(client):
    """Verifies the JSON API endpoint returns correct data"""
    response = client.get('/status')
    assert response.get_json()['status'] == "online"

def test_form_submission_success(client):
    """Verifies successful POST request with form data"""
    response = client.post('/submit', data={'student_name': 'John Doe'})
    assert response.status_code == 201
    assert b'Received: John Doe' in response.data

def test_form_submission_error(client):
    """Verifies 400 error when required data is missing"""
    response = client.post('/submit', data={})
    assert response.status_code == 400
