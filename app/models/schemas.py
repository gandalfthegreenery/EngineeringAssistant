from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class Source(BaseModel):
    document: str
    page: int
    chunk_id: int


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]