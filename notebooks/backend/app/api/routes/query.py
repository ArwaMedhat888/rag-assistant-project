from fastapi import APIRouter

from app.schemas.query import QueryRequest, QueryResponse
from app.services.embedding_service import create_embedding
from app.services.vector_service import search_documents
from app.services.llm_service import generate_answer


router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):

    question = request.question

    embedding = create_embedding(question)

    retrieved = search_documents(embedding, k=3)

    context = ""

    for item in retrieved:
        context += (
            f"Source: {item['source']}, Page: {item['page']}\n"
            f"{item['text']}\n\n"
        )

    answer = generate_answer(context, question)

    return {
        "question": question,
        "answer": answer,
        "sources": [
            {
                "source": item["source"],
                "page": item["page"]
            }
            for item in retrieved
        ]
    }