from fastapi import FastAPI
from backend.router import reminder_router, whisper_router, rag_router, resume_parser_router
from backend.analytics.changed_routers import router as analytics_router  # Import the analytics router
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(rag_router.router, prefix="/rag", tags=["RAG Queries"])
app.include_router(whisper_router.router, prefix="/whisper", tags=["speech to text"])
app.include_router(reminder_router.router, prefix="/reminder", tags=["Reminder"])
app.include_router(resume_parser_router.router, prefix="/document", tags=["Document"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])  # Add analytics router

if __name__ == "__main__":
    print("INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)