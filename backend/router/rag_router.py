from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.rag import run_rag_for_query
router = APIRouter()

class Message(BaseModel):
    message: str

# Changed endpoint from "/rag_route" to "/query" to be more consistent
@router.post("/query/")
async def chat_response(data: Message):
    return {"response": f"You said: {data.message}"}