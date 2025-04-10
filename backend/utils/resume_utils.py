import io
import os
import docx
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import json  # Use json for safer parsing

# Tell pytesseract where the tesseract.exe is located
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Load environment variables
load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_resume(filename: str, file_content: bytes) -> str:
    """
    Extract text from resumes in PDF, DOCX, or image formats.
    """
    if filename.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(file_content))
        text = " ".join(page.extract_text() or "" for page in reader.pages)
        return text.strip()
    
    elif filename.lower().endswith(".docx"):
        doc = docx.Document(io.BytesIO(file_content))
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    
    elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image = Image.open(io.BytesIO(file_content))
        text = pytesseract.image_to_string(image)
        return text.strip()
    
    return ""

def generate_insights_from_text(text: str) -> dict:
    """
    Generate insights from the extracted resume text using the Gemini model.
    """
    prompt = f"""
    You are a smart career guidance system. Read the following resume content and extract:

    - Skills (as a list)
    - Experience (summarized or number of years)
    - Education (highest qualification)
    - 2–3 career suggestions based on the resume

    Resume Text:
    \"\"\"{text}\"\"\" 

    Respond ONLY in JSON format like:
    {{
        "skills": [...],
        "experience": "...",
        "education": "...",
        "career_suggestions": [...]
    }}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        # Remove triple backticks if present
        if raw_output.startswith("```") and raw_output.endswith("```"):
            raw_output = raw_output.strip("```").strip()

        # Remove unwanted prefixes like "json\n"
        if raw_output.startswith("json"):
            raw_output = raw_output[4:].strip()  # Remove "json\n"

        # Parse the cleaned JSON string
        return json.loads(raw_output)
    except json.JSONDecodeError as e:
        return {
            "error": "Failed to parse Gemini response",
            "raw_output": raw_output if 'raw_output' in locals() else "",
            "exception": str(e)
        }
    except Exception as e:
        return {
            "error": "An unexpected error occurred",
            "raw_output": raw_output if 'raw_output' in locals() else "",
            "exception": str(e)
        }

def generate_career_guidance(insights: dict) -> str:
    """
    Generate detailed career guidance based on the extracted insights.
    """
    prompt = f"""
    You are a professional career guidance advisor. Based on the following extracted resume data, provide detailed career guidance:

    - Skills: {", ".join(insights.get("skills", []))}
    - Experience: {insights.get("experience", "Not provided")}
    - Education: {insights.get("education", "Not provided")}
    - Career Suggestions: {", ".join(insights.get("career_suggestions", []))}

    For each career suggestion, provide:
    - A summary of why the candidate is suitable for this role.
    - Detailed steps they can take to achieve this career goal, including skills to improve, certifications to pursue, and networking opportunities.
    - Any additional advice to help them succeed in this role.

    Provide the response in a structured format.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with a valid model
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating career guidance: {str(e)}"