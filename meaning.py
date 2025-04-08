import requests
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_meaning(c):
    word = c.strip().split()[-1]  # Get the last word
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            speak(f"The meaning of {word} is: {meaning}")
            print(f"{word}: {meaning}")
        else:
            speak(f"Sorry, I couldn't find the meaning of {word}")
    except Exception as e:
        speak("Something went wrong.")
        print(f"Error: {e}")
