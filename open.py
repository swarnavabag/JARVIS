import webbrowser
import os

def open_website(c):
        app_web = c.lower().split(" ")[1]
        if "google" in app_web:
            webbrowser.open("https://google.com")
        elif "facebook" in app_web:
            webbrowser.open("https://facebook.com")
        elif "youtube" in app_web:
            webbrowser.open("https://youtube.com")
        elif "linkedin" in app_web:
            webbrowser.open("https://linkedin.com")
        elif "instagram" in app_web:
            webbrowser.open("https://instagram.com")
        elif "twitter" in app_web:
            webbrowser.open("https://twitter.com")
        elif "github" in app_web:
            webbrowser.open("https://github.com")
        elif "stackoverflow" in app_web:
            webbrowser.open("https://stackoverflow.com")
        elif "wikipedia" in app_web:
            webbrowser.open("https://wikipedia.org")
        elif "amazon" in app_web:
            webbrowser.open("https://amazon.in")
        elif "flipkart" in app_web:
            webbrowser.open("https://flipkart.com")
        elif "netflix" in app_web:
            webbrowser.open("https://netflix.com")
        elif "reddit" in app_web:
            webbrowser.open("https://reddit.com")
        elif "pinterest" in app_web:
            webbrowser.open("https://pinterest.com")
        elif "quora" in app_web:
            webbrowser.open("https://quora.com")
        elif "spotify" in app_web:
            webbrowser.open("https://spotify.com")
        elif "x" in app_web:
            webbrowser.open("https://x.com")
        elif "tiktok" in app_web:
            webbrowser.open("https://tiktok.com")
        elif "snapchat" in app_web:
            webbrowser.open("https://snapchat.com")
        elif "telegram" in app_web:
            webbrowser.open("https://telegram.org")
        elif "discord" in app_web:
            webbrowser.open("https://discord.com")
        elif "microsoft" in app_web:
            webbrowser.open("https://microsoft.com")
        elif "github" in app_web:
            webbrowser.open("https://github.com")
        elif "stackoverflow" in app_web:
            webbrowser.open("https://stackoverflow.com")
        elif "calculator" in app_web:
            os.system("calc")
        elif "settings" in app_web:
            os.system("settings")
        elif "notepad" in app_web: 
            os.system("notepad")
        elif "command" in app_web: 
            os.system("cmd")
        elif "chrome" in app_web:  
            os.system("chrome")
        elif "firefox" in app_web:
            os.system("firefox")
        elif "edge" in app_web:
            os.system("msedge")
        elif "word" in app_web:
            os.system("winword")
        elif "powerpoint" in app_web:
            os.system("powerpnt")
        elif "excel" in app_web:
            os.system("excel")
        elif "vlc" in app_web:
            os.system("vlc")
        elif "whatsapp" in app_web:
            os.system("whatsapp")
        elif "zoom" in app_web: 
            os.system("zoom")
        elif "teams" in app_web:
            os.system("teams")