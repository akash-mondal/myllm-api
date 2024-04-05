from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.post("/ask")
async def generate_response(user_input: str):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    payload = {
      "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
      "max_tokens": 4096,
      "top_p": 1,
      "top_k": 40,
      "presence_penalty": 0,
      "frequency_penalty": 0,
      "temperature": 0.6,
      "messages": [
        {
          "role": "user",
          "content": user_input
        }
      ]
    }
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": "Bearer 3J2VhOCg9nJF30zpLUJvlALsMAM0zG6b9KjJf1PhX7mx7GIn"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        llm_response = response.json()['choices'][0]['message']['content']
        return llm_response
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to generate response")
