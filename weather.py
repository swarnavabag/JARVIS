import pyttsx3
import requests

engine = pyttsx3.init()
weatherapikey = "9b7a5bf8aea74f05bae161943250704"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather(c):
    c = c.lower()
    city = c.split(" ")[-1]
    url = f"http://api.weatherapi.com/v1/current.json?key={weatherapikey}&q={city}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        location = data['location']['name']
        report = f"The weather in {location} is {condition} with a temperature of {temp} degree Celsius."
        print(report)
        speak(report)
    else:
        speak("Sorry, I couldn't get the weather data right now.")
