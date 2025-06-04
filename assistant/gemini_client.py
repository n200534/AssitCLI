import os
import requests
from config import get_gemini_api_key

def generate_text_with_gemini(prompt: str) -> str:
    api_key = get_gemini_api_key()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Gemini API error {response.status_code}: {response.text}")
    
    response_json = response.json()
    
    # Extract the generated content
    candidates = response_json.get("candidates", [])
    if not candidates:
        return ""
    
    # Get the content object
    content = candidates[0].get("content", {})
    if not content:
        return ""
    
    # Get the parts array
    parts = content.get("parts", [])
    if not parts:
        return ""
    
    # Get the text from the first part
    text = parts[0].get("text", "")
    
    return text