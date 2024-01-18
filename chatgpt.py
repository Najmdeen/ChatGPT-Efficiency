import requests
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def query_chatgpt(message):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7  # Adjust as needed
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json()
