from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vector_store import vector_store
from app.services.llm_service import llm_service
from typing import List, Optional, Dict, Any

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    tool_context: Optional[Dict[str, Any]] = None

class IngestRequest(BaseModel):
    texts: List[str]

@router.post("/message", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # 1. Retrieve relevant docs
        docs = vector_store.search(request.message)
        
        # 2. Generate answer
        result = llm_service.generate_answer(request.message, docs)
        
        return ChatResponse(
            answer=result["answer"],
            sources=[d.get('text', '')[:50] + "..." for d in docs],
            tool_context=result.get("tool_context")
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ingest")
def ingest(request: IngestRequest):
    vector_store.upsert_documents(request.texts)
    return {"status": "success", "count": len(request.texts)}
