import google.generativeai as genai
import os
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

try:
    with open("models.txt", "w") as f:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                f.write(m.name + "\n")
    print("Models written to models.txt")
except Exception as e:
    print(f"Error: {e}")
