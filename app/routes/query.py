from fastapi import APIRouter
from pydantic import BaseModel
from app.services.retriever import retrieve_relevant_chunks
from app.services.llm import generate_answer

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    chat_history: list = []


@router.post("/query")
async def query_documents(request: QueryRequest):

    # Retrieve relevant chunks
    results = retrieve_relevant_chunks(request.question)

    # Generate conversational answer
    answer = generate_answer(
        request.question,
        results,
        request.chat_history
    )

    return {
        "question": request.question,
        "answer": answer,
        "retrieved_chunks": results
    }