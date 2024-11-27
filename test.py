import pytest
from main import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert "Väder i" in response.data.decode('utf-8')  # Dekodera bytes till sträng
