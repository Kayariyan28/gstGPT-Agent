import google.generativeai as genai
import os
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

try:
    print("Listing models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error: {e}")
