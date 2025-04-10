from fastapi import FastAPI
# from backend.models import rag
from backend.router import reminder_router, whisper_router, rag_router
# import uvicorn
app = FastAPI()

app.include_router(rag_router.router, prefix="/rag", tags=["RAG Queries"])
app.include_router(whisper_router.router, prefix="/whisper", tags=["speech to text"])
app.include_router(reminder_router.router, prefix="/reminder", tags=["Reminder"])
# if __name__ == "__main__":
#     print("🟢 StartinRecording and transcribing...g FastAPI app with Uvicorn...")
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
