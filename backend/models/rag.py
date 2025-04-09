# import requests
# from bs4 import BeautifulSoup
# import chromadb
# from sentence_transformers import SentenceTransformer
# import google.generativeai as genai

# # --- Extract text from a website ---
# def extract_text_from_website(url):
#     try:
#         response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, "html.parser")
#         paragraphs = soup.find_all("p")
#         return " ".join([p.get_text() for p in paragraphs]) if paragraphs else "No content available."
#     except requests.RequestException as e:
#         print(f"Error fetching {url}: {e}")
#         return "Error fetching content."


# def load_dataset_chunks(file_path, chunk_size=100):
#     try:
#         df = pd.read_csv(file_path)
#         all_text = df.astype(str).apply(" ".join, axis=1).tolist()
        
#         # Split into smaller chunks
#         chunks = []
#         for i in range(0, len(all_text), chunk_size):
#             chunk = " ".join(all_text[i:i + chunk_size])
#             chunks.append(chunk)
#         return chunks
#     except Exception as e:
#         print(f"Error loading dataset: {e}")
#         return []
    
    
# # --- Configuration ---
# career_urls = [
#     "https://leverageedu.com/blog/how-to-become-an-architect/",
#     "https://leverageedu.com/blog/film-actor/",
#     "https://leverageedu.com/blog/career-in-animation/",
#     "https://leverageedu.com/blog/how-to-join-indian-army/",
#     "https://leverageedu.com/blog/career-as-a-banker/",
#     "https://leverageedu.com/blog/dance-schools/",
#     "https://leverageedu.com/blog/how-to-become-a-doctor/",
#     "https://leverageedu.com/blog/category/engineering/",
#     "https://leverageedu.com/blog/career-in-fashion-designing/",
#     "https://leverageedu.com/blog/how-to-become-a-journalist/",
#     "https://leverageedu.com/blog/how-to-become-a-lawyer/",
#     "https://leverageedu.com/blog/category/mba/",
#     "https://leverageedu.com/blog/how-to-become-a-commercial-pilot/",
#     "https://leverageedu.com/blog/criminology-courses/",
#     "https://leverageedu.com/blog/types-of-mass-media/",
#     "https://leverageedu.com/blog/how-to-become-a-scientist/",
#     "https://leverageedu.com/blog/category/sports-management/",
#     "https://leverageedu.com/blog/how-to-become-a-veterinary-doctor/",
#     "https://leverageedu.com/blog/how-to-be-a-content-writer/",
#     "https://leverageedu.com/blog/career-in-fashion-designing/",
#     "https://leverageedu.com/blog/career-in-hotel-management/",
#     "https://leverageedu.com/blog/product-design/",
#     "https://leverageedu.com/blog/bakery-and-confectionery/",
#     "https://leverageedu.com/blog/graphology/",
#     "https://leverageedu.com/blog/how-to-become-a-professor/",
#     "https://leverageedu.com/blog/civil-engineer/",
#     "https://leverageedu.com/blog/electrical-engineer/",
#     "https://leverageedu.com/blog/how-to-become-an-aerospace-engineer/",
#     "https://leverageedu.com/blog/automobile-engineering/",
#     "https://leverageedu.com/blog/category/chartered-accountancy/",
#     "https://www.lpu.in/blog/top-career-options-after-12th-science-pcm-best-opportunities-paths/",
#     "https://nexisschool.com/career-options-after-12th/",
#     "https://www.upgrad.com/blog/top-career-options-after-engineering/"
# ]

# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Initialize ChromaDB
# chroma_client = chromadb.PersistentClient(path="./career_db")
# collection = chroma_client.get_or_create_collection(name="career_guidance")

# # Add documents to ChromaDB if not already present
# existing_ids = set(collection.get()["ids"])
# for url in career_urls:
#     if url not in existing_ids:
#         text = extract_text_from_website(url)
#         embedding = model.encode(text).tolist()
#         collection.add(ids=[url], documents=[text], embeddings=[embedding])

# # Configure Gemini
# genai.configure(api_key="AIzaSyCYYUDOTqdhMC_NDbrQS-htFND7vocAIes")

# conversation_history = []

# # --- Main RAG Function ---
# def run_rag_for_query(query):
#     print(f"Running RAG for query: {query}")  # Add this
#     query_embedding = model.encode(query).tolist()
#     results = collection.query(query_embeddings=[query_embedding], n_results=1)

#     if not results["documents"]:
#         print("No documents found!")  # Add this
#         return "Sorry, I couldn't find relevant information."

#     matched_texts = "\n\n".join(results["documents"][0])
#     print("Matched text:", matched_texts[:500])  # Preview the matched content

#     conversation_history.append(f"User Query: {query}")

#     system_prompt = """
#     # You are a professional career guidance advisor.
#     # Based on the provided extracted text, respond with:
#     # - Clear, structured, and step-by-step guidance.
#     # - Career related accurate information without unnecessary details.
#     # - Avoid * and use - for bullet points.
#     # - Maintain a friendly and supportive tone.
#     # - Provide a summary of the extracted information. 
#     # - If the user asks for a specific career path, provide detailed information about that path.
#     # - If the user asks for general career advice, provide a well-rounded response based on the extracted information.
#     - You are a informatic professional.
#     """

#     user_prompt = f"User Query: {query}\n\nExtracted Information:\n{matched_texts}\n\nHistory:\n{conversation_history}"

#     model_gemini = genai.GenerativeModel("gemini-1.5-flash")
#     response = model_gemini.generate_content(system_prompt + "\n\n" + user_prompt)

#     conversation_history.append(f"AI Response: {response.text.strip()}")
#     return response.text.strip()

# # --- CLI entry point ---
# print("Script started...")  # Add this line
# query = input("Enter your query: ")
# if not query:
#     print("No query provided. Exiting...")
#     exit(1)
# response = run_rag_for_query(query)
# print("Guidance:\n", response)



import requests
from bs4 import BeautifulSoup
from datasets import load_dataset
import chromadb
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import whisper  # Import Whisper for speech-to-text
import sounddevice as sd
import numpy as np
from backend.models.whisper import record_and_transcribe
# --- Whisper Speech-to-Text Function ---
# def get_speech_input():
#     print("Listening... Speak your query.")
#     model = whisper.load_model("base")
#     duration = 5  # Record for 5 seconds
#     sample_rate = 16000
#     print("Recording...")
#     audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
#     sd.wait()
#     print("Processing audio...")
#     audio = np.squeeze(audio)
#     result = model.transcribe(audio)
#     return result["text"]

# --- Extract text from website ---
def extract_text_from_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.get_text() for p in paragraphs]) if paragraphs else "No content available."
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

# --- Load dataset from Hugging Face and chunk ---
def load_hf_dataset_chunks(dataset_path="Pradeep016/career-guidance-qa-dataset", chunk_size=10):
    try:
        dataset = load_dataset(dataset_path, split="train")  # Automatically gets the CSV
        rows = [f"{row['question']} {row['answer']}" for row in dataset if row['question'] and row['answer']]
        
        chunks = []
        for i in range(0, len(rows), chunk_size):
            chunk = " ".join(rows[i:i + chunk_size])
            chunks.append(chunk)
        return chunks
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return []

# --- Configuration ---
career_urls = [
    "https://leverageedu.com/blog/how-to-become-an-architect/",
    "https://leverageedu.com/blog/film-actor/",
    "https://leverageedu.com/blog/career-in-animation/",
    "https://leverageedu.com/blog/how-to-join-indian-army/",
    "https://leverageedu.com/blog/career-as-a-banker/",
    "https://leverageedu.com/blog/dance-schools/",
    "https://leverageedu.com/blog/how-to-become-a-doctor/",
    "https://leverageedu.com/blog/category/engineering/",
    "https://leverageedu.com/blog/career-in-fashion-designing/",
    "https://leverageedu.com/blog/how-to-become-a-journalist/",
    "https://leverageedu.com/blog/how-to-become-a-lawyer/",
    "https://leverageedu.com/blog/category/mba/",
    "https://leverageedu.com/blog/how-to-become-a-commercial-pilot/",
    "https://leverageedu.com/blog/criminology-courses/",
    "https://leverageedu.com/blog/types-of-mass-media/",
    "https://leverageedu.com/blog/how-to-become-a-scientist/",
    "https://leverageedu.com/blog/category/sports-management/",
    "https://leverageedu.com/blog/how-to-become-a-veterinary-doctor/",
    "https://leverageedu.com/blog/how-to-be-a-content-writer/",
    "https://leverageedu.com/blog/career-in-fashion-designing/",
    "https://leverageedu.com/blog/career-in-hotel-management/",
    "https://leverageedu.com/blog/product-design/",
    "https://leverageedu.com/blog/bakery-and-confectionery/",
    "https://leverageedu.com/blog/graphology/",
    "https://leverageedu.com/blog/how-to-become-a-professor/",
    "https://leverageedu.com/blog/civil-engineer/",
    "https://leverageedu.com/blog/electrical-engineer/",
    "https://leverageedu.com/blog/how-to-become-an-aerospace-engineer/",
    "https://leverageedu.com/blog/automobile-engineering/",
    "https://leverageedu.com/blog/category/chartered-accountancy/",
    "https://www.lpu.in/blog/top-career-options-after-12th-science-pcm-best-opportunities-paths/",
    "https://nexisschool.com/career-options-after-12th/",
    "https://www.upgrad.com/blog/top-career-options-after-engineering/",
    "https://idreamcareer.com/blog/career-options-in-art/",
    "https://idreamcareer.com/blog/career-options-after-12th/#Career_Options_After_12th_PCM",
    "https://idreamcareer.com/blog/courses-after-12th-pcm/",
    "https://idreamcareer.com/blog/which-career-has-more-scope-in-future/",
    "https://idreamcareer.com/blog/career-in-travel-and-tourism-2/",
    "https://idreamcareer.com/blog/career-in-finance/",
    "https://idreamcareer.com/blog/business-courses-after-12th/"
    "https://idreamcareer.com/blog/how-to-become-a-doctor-in-india/",
    "https://idreamcareer.com/career/career-as-a-pharmacists/",
    "https://idreamcareer.com/blog/lab-technician-course-after-12th/",
    "https://idreamcareer.com/blog/mass-communication-courses-after-12th/",
    "https://idreamcareer.com/blog/how-to-become-a-psychologist/",
    "https://idreamcareer.com/blog/best-career-options-after-12th-science/"
]

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./career_db")
collection = chroma_client.get_or_create_collection(name="career_guidance")
existing_ids = set(collection.get()["ids"])

# --- Add website data ---
for url in career_urls:
    if url not in existing_ids:
        text = extract_text_from_website(url)
        if text:
            embedding = model.encode(text).tolist()
            collection.add(ids=[url], documents=[text], embeddings=[embedding])

# --- Add Hugging Face dataset data ---
dataset_chunks = load_hf_dataset_chunks()
for i, chunk in enumerate(dataset_chunks):
    chunk_id = f"hf_dataset_chunk_{i}"
    if chunk_id not in existing_ids and chunk.strip():
        embedding = model.encode(chunk).tolist()
        collection.add(ids=[chunk_id], documents=[chunk], embeddings=[embedding])

# --- Gemini Config ---
genai.configure(api_key="AIzaSyCYYUDOTqdhMC_NDbrQS-htFND7vocAIes")
conversation_history = []

# --- RAG Logic ---
def run_rag_for_query(query):
    print(f"Running RAG for query: {query}")
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=5)

    if not results["documents"]:
        return "Sorry, no relevant information found."

    matched_texts = "\n\n".join([doc for doc_list in results["documents"] for doc in doc_list])
    conversation_history.append(f"User Query: {query}")

    system_prompt = """
    You are a professional career guidance advisor.
    - Provide structured, step-by-step, and easy-to-follow guidance.
    - Summarize and merge info from websites and datasets accurately.
    - Avoid * and use - for bullet points.
    - Stay friendly and helpful.
    - If there is no related information in the provided documents, add your own knowledge.
    - Provide a summary of the extracted information.
    - Generate every response for an Indian student. Don't mention any other country or information for career guidance.
    - Add your own knowledge in the generated response. Don't totally stick to my provided documents.
    """

    user_prompt = f"User Query: {query}\n\nExtracted Information:\n{matched_texts}\n\nHistory:\n{conversation_history}"
    model_gemini = genai.GenerativeModel("gemini-1.5-flash")
    response = model_gemini.generate_content(system_prompt + "\n\n" + user_prompt)

    conversation_history.append(f"AI Response: {response.text.strip()}")
    return response.text.strip()



# --- CLI Entry ---
print("Script started...")
input_method = input("Would you like to speak or type your query? (speak/type): ").strip().lower()

if input_method == "speak":
    query = record_and_transcribe()
elif input_method == "type":
    query = input("Enter your career-related question: ")
else:
    print("Invalid input method selected. Exiting...")
    exit(1)

if query:
    response = run_rag_for_query(query)
    print("\n--- Guidance ---\n", response)
else:
    print("No query entered.")