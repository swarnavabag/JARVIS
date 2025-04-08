import speech_recognition as sr
import pyttsx3
import requests
import musiclibrary
import ai_assistance
import newslibrary
import open
import weather
import date_time
import google_search
import meaning

r=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    if "open" in c.lower():
        open.open_website(c)
    elif "play" in c.lower():
            musiclibrary.song_search(c)
    elif "news" in c.lower():
        newslibrary.get_news()
    elif "ai" in c.lower():
        print("AI activated")
        speak("Yes sir, What can I do For You?")
        with sr.Microphone() as source:
                    audio = r.listen(source, timeout=4,phrase_time_limit=10)
                    prompt = r.recognize_google(audio)
        
                    print(prompt)
        ai_assistance.ask_ai(prompt)
    elif "weather of" in c.lower():
        weather.get_weather(c)
    elif "time" in c.lower() or "date" in c.lower():
        date_time.tell_date_time(c)
    elif "google search" in c.lower():
        google_search.googlesearch(c)
    elif "greet" in c.lower():
        speak("Hello Sir, You are looking great today.")
    elif "my location" in c.lower():
        ip_data = requests.get("https://ipinfo.io").json()
        print(ip_data["city"], ip_data["region"], ip_data["country"])
    elif "meaning" in c.lower():
        meaning.get_meaning(c)
    elif "exit" in c.lower() or "stop" in c.lower() or "quit" in c.lower():
        print("Exiting...")
        speak("Exiting...")
        exit()
    


if __name__ == "__main__":
    print("initializing Jarvis...")
    speak("initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                speak("Listening...")
                audio = r.listen(source, timeout=3,phrase_time_limit=2)
            print("Recognizing...")
            word =r.recognize_google(audio)
            print(word)

            if "jarvis" in word.lower():
                print("Jarvis activated")
                speak("Yes sir, What can I do For You?")
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=4,phrase_time_limit=10)
                    command = r.recognize_google(audio)
                    print(command)
                process(command)  


        except Exception as e:
            print("Sorry, I didn't get that. Try again please")