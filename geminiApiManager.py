from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()

def completionRequest(prompt):
    """
    Request the LLM with the argument of the function
    
    Args:
        prompt (str): instruction for the LLM
        
    Returns:
        str: Response of the LLM
    """
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt,
    )

    return response.text
