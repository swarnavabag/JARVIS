import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

r=sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "03fa5cd2b223efd8cd52859a5f161da6"
url = f"http://api.mediastack.com/v1/news?access_key={newsapi}&countries=in&languages=en&limit=5"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    if "open" in c.lower():
        if "google" in c.lower():
            webbrowser.open("https://google.com")
        elif "facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)
    elif "news" in c.lower():
        speak("Fetching news...")
        r = requests.get(url)
        data = r.json()
        articles = data.get("data", [])

        if articles:
            for article in articles:
                title = article.get("title")
                if title:
                    print(f"News: {title}")
                    speak(title)
        else:
            speak("Sorry, no news found right now.")
    else:
        
        

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
                    audio = r.listen(source, timeout=3,phrase_time_limit=8)
                    command = r.recognize_google(audio)

                process(command)  


        except Exception as e:
            print("Sorry, I didn't get that. Try again please")