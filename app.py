import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("AIzaSyCeEIFvNCyc4oAJpK1Vluh3lCiMea0nyaI")

if not api_key:
    raise Exception("Gemini API Key not found. Set GEMINI_API_KEY in .env.")

# Configure Gemini client
genai.configure(api_key=api_key)

# Create a Gemini Pro model instance
model = genai.GenerativeModel('gemini-pro')

# Define a prompt for generating a meme caption
prompt = "Write a short, funny meme caption about programmers and bugs."

# Generate content
response = model.generate_content(prompt)

# Print result
print("💡 Generated Meme Caption:")
print(response.text.strip())
