import datetime
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_date_time(c):
    c = c.lower()
    now = datetime.datetime.now()
    date = now.strftime("%d %B %Y")
    time = now.strftime("%I:%M %p")

    if "date" or "time" in c:
        print(f"Date: {date} & Time: {time}")
        speak(f"Date is  {date} & Time is {time}")