import io
import os
import docx
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_resume(filename: str, file_content: bytes) -> str:
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
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        result = response.text.strip()

        return eval(result)  # If you're worried about safety, use `json.loads()` with stricter validation
    except Exception as e:
        return {
            "error": "Failed to parse Gemini response",
            "raw_output": result if 'result' in locals() else "",
            "exception": str(e)
        }
