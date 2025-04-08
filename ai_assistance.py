import speech_recognition as sr
import requests
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

aiapi = "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"

def ask_ai(question):
    headers = {
    "Authorization": f"Bearer {aiapi}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    }

    prompt = f"Answer this question clearly and briefly: {question}"
    
    data = {
    "model": "mistralai/mistral-7b-instruct", 
    "messages": [
        {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        print("AI says:", reply)
        speak(reply)
    else:
        print("Error:", response.status_code)
        speak("Error:", response.status_code)