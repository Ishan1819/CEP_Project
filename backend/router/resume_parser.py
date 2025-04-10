from fastapi import APIRouter, UploadFile, File
from utils.resume_utils import extract_text_from_resume, generate_insights_from_text
from fastapi.responses import JSONResponse
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()
router = APIRouter()

@router.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Step 1: Extract text from uploaded resume
        contents = await file.read()
        text = extract_text_from_resume(file.filename, contents)
        
        if not text:
            return JSONResponse(status_code=400, content={"error": "Unable to extract text from document."})

        # Step 2: Generate structured info + suggestion
        result = generate_insights_from_text(text)

        return JSONResponse(status_code=200, content=result)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
