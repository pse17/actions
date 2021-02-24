import pytest
import main
import os
import tempfile

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    with main.app.test_client() as client:
        yield client

def test_home(client):
    resp = client.get('/')
    assert b'Hello !' in resp.data
