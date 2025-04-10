from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.rag import run_rag_for_query

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/query/")
async def chat_response(data: Message):
    response = run_rag_for_query(data.message)
    return {"query": data.message, "guidance": response}