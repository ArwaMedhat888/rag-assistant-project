from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class Source(BaseModel):
    source: str
    page: int


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]