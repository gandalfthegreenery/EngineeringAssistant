from fastapi import APIRouter
from ..models.schemas import QueryRequest, QueryResponse
from ..services.rag_service import orchestrator

router = APIRouter(prefix="/query",tags=["query"])


@router.post("/",response_model=QueryResponse)
def query_documents(request:QueryRequest):
    return orchestrator(
        query=request.question, top_k=request.top_k
)