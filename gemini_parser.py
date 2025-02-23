import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def parse_resume(resume_text):
    """Parse resume text using Gemini API"""
    prompt = f"""Please analyze this resume text and extract the following information in JSON format:
    {resume_text}
    
    Please extract:
    1. Skills
    2. Work Experience
    3. Education
    4. Key Achievements
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error parsing resume with Gemini API: {e}")
        return None