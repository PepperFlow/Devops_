import pytest
from main import app

def test_home():
    # Testar att huvudsidan laddas korrekt
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert "Ange stad" in response.data.decode('utf-8')  

def test_invalid_city():
    # Testar felhantering för ogiltig stad
    with app.test_client() as client:
        response = client.get('/?city=ogiltigstad')
        assert response.status_code == 200
        assert "Staden hittades inte. Försök igen." in response.data.decode('utf-8')  

if __name__ == "__main__":
    pytest.main()
