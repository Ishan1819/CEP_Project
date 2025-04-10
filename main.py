from fastapi import FastAPI
from backend.router import reminder_router, whisper_router, rag_router
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.include_router(rag_router.router, prefix="/rag", tags=["RAG Queries"])
app.include_router(whisper_router.router, prefix="/whisper", tags=["speech to text"])
app.include_router(reminder_router.router, prefix="/reminder", tags=["Reminder"])

if __name__ == "__main__":
    print("INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)