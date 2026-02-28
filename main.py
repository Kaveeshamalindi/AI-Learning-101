import os
from dotenv import load_dotenv
from google import genai

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("api_key")

client = genai.Client(api_key=API_KEY)

def generate(prompt):
    response = client.models.generate_content(
     model="gemini-3-flash-preview", contents=prompt
    )
    return response.text 

answer = generate("Who is Goger S. Pressman ?") 
print(answer)