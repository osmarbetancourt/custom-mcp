import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_and_get_context():
    # Add a context document
    response = client.post("/context", json={"content": "Test context"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["content"] == "Test context"
    doc_id = data["id"]

    # Get the context document
    response = client.get(f"/context/{doc_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == doc_id
    assert data["content"] == "Test context"

def test_delete_context():
    # Add a context document
    response = client.post("/context", json={"content": "To be deleted"})
    doc_id = response.json()["id"]

    # Delete the context document
    response = client.delete(f"/context/{doc_id}")
    assert response.status_code == 200
    assert response.json()["deleted"] == doc_id

    # Try to get the deleted document
    response = client.get(f"/context/{doc_id}")
    assert response.status_code == 404

def test_query_endpoint():
    response = client.post("/query", json={"query": "Hello?", "context_ids": []})
    assert response.status_code == 200
    data = response.json()
    assert data["response"].startswith("Echo: ")
