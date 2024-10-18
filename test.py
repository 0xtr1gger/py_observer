import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """
    Test the home route.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to PyObserver!" in response.data

def test_cpu(client):
    """
    Test the CPU info route.
    """
    response = client.get('/cpu')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, dict)
    assert 'Physical cores' in json_data
    assert 'Total cores' in json_data
    assert 'CPU usage per core' in json_data
    assert 'CPU frequency' in json_data
    assert 'Total CPU usage' in json_data


def test_platform(client):
    """
    Test the platform info route.
    """
    response = client.get('/platform')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, dict)
    assert 'Operating System' in json_data
    assert 'OS version' in json_data
    assert 'OS release' in json_data
    assert 'Machine' in json_data
    assert 'Platform Architecture' in json_data
    assert 'Platform Architecture' in json_data
