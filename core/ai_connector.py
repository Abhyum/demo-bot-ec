import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Setup Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception(" GEMINI_API_KEY not found. Please check your .env file.")

# Configure Gemini Client
genai.configure(api_key=GEMINI_API_KEY)

# Create Gemini Model
model = genai.GenerativeModel('gemini-1.5-flash')  # You can change to 'gemini-pro' later if needed

def generate_response(prompt):
    """
    Simple function to interact with Gemini model
    (for initial testing without LangChain tools)
    """
    response = model.generate_content(prompt)
    return response.text