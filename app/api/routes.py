from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional


import uuid

router = APIRouter()

# In-memory storage for context documents
context_store = {}

# Models
class QueryRequest(BaseModel):
    query: str
    context_ids: Optional[List[str]] = None

class QueryResponse(BaseModel):
    response: str
    context: Optional[List[str]] = None

class ContextDocument(BaseModel):
    id: Optional[str] = None
    content: str

# Endpoints
@router.post("/query", response_model=QueryResponse)
def submit_query(request: QueryRequest):
    # Placeholder logic
    return QueryResponse(response=f"Echo: {request.query}", context=request.context_ids)

@router.post("/context", response_model=ContextDocument)
def add_context(doc: ContextDocument):
    # Generate a unique ID for the new document
    doc_id = str(uuid.uuid4())
    doc.id = doc_id
    context_store[doc_id] = doc.content
    return doc

@router.get("/context/{doc_id}", response_model=ContextDocument)
def get_context(doc_id: str):
    # Retrieve the document from the store
    content = context_store.get(doc_id)
    if content is None:
        raise HTTPException(status_code=404, detail="Context document not found")
    return ContextDocument(id=doc_id, content=content)

@router.delete("/context/{doc_id}")
def delete_context(doc_id: str):
    # Delete the document from the store
    if doc_id in context_store:
        del context_store[doc_id]
        return {"deleted": doc_id}
    else:
        raise HTTPException(status_code=404, detail="Context document not found")
