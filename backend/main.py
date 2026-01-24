# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Chat(BaseModel):
    message: str

HISTORY_FILE = "chathistory.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.post("/chat")
def chat(data: Chat):
    hf_api_key = os.getenv("HF_API_KEY")
    if not hf_api_key:
        return {"reply": "HF_API_KEY is not set!"}

    # Router Chat API (OpenAI-compatible)
    url = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {hf_api_key}",
        "Content-Type": "application/json"
    }

    history = load_history()
    history.append({"role": "user", "content": data.message})

    messages = []
    for msg in history[-10:]:
        role = "assistant" if msg["role"] == "bot" else "user"
        messages.append({
            "role": role,
            "content": msg["content"]
    })


    payload = {
        "model": "openai/gpt-oss-120b",  # pick a working model
        "messages": messages,
        "max_tokens": 150,
        "temperature": 0.7
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        result = r.json()

        reply = result["choices"][0]["message"]["content"]

        history.append({"role": "bot", "content": reply})
        save_history(history)

        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Error: {e}"}
