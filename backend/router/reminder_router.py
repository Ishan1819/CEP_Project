from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.reminder import schedule_email

router = APIRouter()

# Create a Pydantic model for request body validation
class ReminderRequest(BaseModel):
    reminder_text: str
    time_str: str

@router.post("/schedule_reminder/")
async def schedule_reminder(request: ReminderRequest):
    if request.reminder_text == "remind me":
        return {"message": "Reminder text cannot be empty."}
    schedule_email(request.reminder_text, request.time_str)
    return {"message": "Reminder scheduled successfully."}