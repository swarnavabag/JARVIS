
import requests
from mega_proj_1 import speak

newsapi = "03fa5cd2b223efd8cd52859a5f161da6"
url = f"http://api.mediastack.com/v1/news?access_key={newsapi}&countries=in&languages=en&limit=5"

def get_news():
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