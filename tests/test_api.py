from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, create_tables
import pytest

client = TestClient(app)

# Testeo a BD
@pytest.fixture(scope="module")
def test_db():
    # Creación de tablas en la BD test
    create_tables()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Testeo del endpoint que analiza los cometarios
def test_analyze_multiple_sentiments():
    comments = [
        "I love this phone, the camera is amazing.",
        "The product is decent, but not worth the price.",
        "This is the worst service I've ever encountered.",
        "La nintendo Switch 2 es excelente",
        "Mi nueva asus es genial"
    ]
    response = client.post("/analyze_sentiment/", json=comments)
    assert response.status_code == 200
    data = response.json()
    assert data["overall_sentiment"] in ["positive", "negative", "neutral"]
    assert "details" in data


# Test a endpoint que obtiene todos los registros
def test_read_sentiments():
    response = client.get("/sentiments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test a endpoint que borra registro por id
def test_delete_sentiment():
    # primero se agrega texto a analizar
    response = client.post("/analyze_sentiment/", json=["Test comment for deletion"])
    assert response.status_code == 200
    
    # se recupera registro por id
    sentiments = client.get("/sentiments/").json()
    sentiment_id = sentiments[-1]["id"]
    
    # Testeo del borrado p or id
    delete_response = client.delete(f"/sentiments/{sentiment_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "Sentiment deleted successfully"}


# Test de borrado de todos los registros
def test_delete_all_sentiments():
    # aquí se asegura que haya registros por borrar
    client.post("/analyze_sentiment/", json=["Comment 1", "Comment 2"])
    response = client.delete("/sentiments/")
    assert response.status_code == 200
    assert response.json() == {"detail": "All sentiments deleted successfully"}
    
    # testeo del borrado total de los registros en BD
    get_response = client.get("/sentiments/")
    assert get_response.status_code == 200
    assert get_response.json() == []
