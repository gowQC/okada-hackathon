from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.rag import get_relevant_context
from app.services.llm import ask_llm

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(req: ChatRequest):
    query = req.message

    # Step 1: Retrieve relevant context from Chroma
    context = get_relevant_context(query)

    # Step 2: Ask the LLM using both query and retrieved context
    response = await ask_llm(query, context)

    return {"response": response}
