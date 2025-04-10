import re  # Import the re module for splitting with multiple delimiters
from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.rag import run_rag_for_query
from backend.models.reminder import schedule_email
# import router

router = APIRouter()

@router.get("/")
async def read_rag():
    return {"message": "RAG endpoint"}
class Message(BaseModel):
    message: str

@router.post("/query/")
async def chat_response(data: Message):
    query = data.message.strip()

    # Check if "remind me" exists anywhere in the query
    if "remind me" in query.lower():
        try:
            # Extract the reminder text and time using regex to split by multiple delimiters
            parts = re.split(r" at | after | in ", query.lower(), maxsplit=1)
            if len(parts) != 2:
                return {"error": "Invalid format. Use 'remind me [text] at [time]'."}

            reminder_text = parts[0].replace("remind me", "").strip()
            time_str = parts[1].strip()

            # Schedule the email
            schedule_email(reminder_text, time_str)
            return {"message": "Reminder scheduled successfully.", "reminder_text": reminder_text, "time": time_str}
        except Exception as e:
            return {"error": f"Failed to schedule reminder: {str(e)}"}

    # If "remind me" is not in the query, process it normally
    response = run_rag_for_query(query)
    return {"response": response}