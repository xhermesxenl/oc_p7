import pytest
from flask.testing import FlaskClient
from api import app  # Assurez-vous que ce chemin est correct

# Configuration du client de test Flask
@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

# Test de la route racine          
def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenue dans l'API de prédiction de crédit !" in response.data.decode()

# Test de la route de prédiction avec une requête POST valide
def test_predict_credit_valid(client):

    id_accept = 144194

    response = client.get(f"/api/predict/{id_accept}")
    assert response.status_code == 200
    assert "probability" in response.json
    assert "classe" in response.json
    assert response.json["classe"] in ["accepte"]


# Test de la route de prédiction avec une requête POST invalide
def test_predict_credit_invalid(client):

    id_refuse = 13112
    response = client.get(f"/api/predict/{id_refuse}")
    assert response.status_code == 200
    assert "probability" in response.json
    assert "classe" in response.json
    assert response.json["classe"] in ["refuse"]


# Test de la route de prédiction avec une requête POST invalide
def test_predict_credit_unknown(client):

    id_unknow = 999999
    response = client.get(f"/api/predict/{id_unknow}")

    assert response.status_code == 404
    assert "error" in response.json
    assert response.json["error"] == "Unknown ID"