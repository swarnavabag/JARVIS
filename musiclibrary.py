import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

music = {
    "tera zikr": "https://www.youtube.com/watch?v=eK0IIyBlYew",
    "pasoori": "https://www.youtube.com/watch?v=5Eqb_-j3FDA",
    "kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs",
    "malang sajna": "https://www.youtube.com/watch?v=UbMgcdmYC70",
    "heeriye": "https://www.youtube.com/watch?v=RLzC55ai0eo",
    "raataan lambiyan": "https://www.youtube.com/watch?v=gvyUuxdRdR4",
    "tum mile": "https://www.youtube.com/watch?v=jC1dHOCmGxo",
    "tum hi ho": "https://www.youtube.com/watch?v=Umqb9KENgmk",
    "apna bana le": "https://www.youtube.com/watch?v=3pz_bHeZLkg",
    "shayad": "https://www.youtube.com/watch?v=MJyKN-8UncM",
    "bones": "https://www.youtube.com/watch?v=TO-_3tck2tg",
    "enemy": "https://www.youtube.com/watch?v=hHB1Ikzfpmc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "unstoppable": "https://www.youtube.com/watch?v=YaEG2aWJnZ8",
    "attention": "https://www.youtube.com/watch?v=nfs8NYg7yQM",
    "industry baby": "https://www.youtube.com/watch?v=UTHLKHL_whs",
    "let me down slowly": "https://www.youtube.com/watch?v=50VNCymT-Cs",
    "counting stars": "https://www.youtube.com/watch?v=hT_nvWreIhg",
    "night changes": "https://www.youtube.com/watch?v=syFZfO_wfMQ",
    "dandelions": "https://www.youtube.com/watch?v=A1cFoOP5EkY",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "love me like you do": "https://www.youtube.com/watch?v=AJtDXIazrMo",
    "heat waves": "https://www.youtube.com/watch?v=mRD0-GxqHVo",
    "arcade": "https://www.youtube.com/watch?v=Qau6mObfSGM",
    "pehla nasha": "https://www.youtube.com/watch?v=SBfPs-PMGTA",
    "tu hi re": "https://www.youtube.com/watch?v=P4NwOb39sTQ",
    "chura ke dil mera": "https://www.youtube.com/watch?v=Yqj1_V90KJo",
    "didi tera devar deewana": "https://www.youtube.com/watch?v=ZqcDGvCM_w0",
    "mera dil bhi kitna pagal hai": "https://www.youtube.com/watch?v=DIvHIjOYq3U",
    "raah mein unse mulaqat": "https://www.youtube.com/watch?v=vYGPudMvxvI",
    "tumse milne ki tamanna hai": "https://www.youtube.com/watch?v=3nytZXLMRsg",
    "jab koi baat bigad jaye": "https://www.youtube.com/watch?v=ln3meCI0LFM",
    "tip tip barsa pani": "https://www.youtube.com/watch?v=VEOBiDB1Fxk",
    "tum to dhokebaaz o": "https://www.youtube.com/watch?v=tUQ_10aNcAE"
}

def song_search(c):
    song = " ".join(c.lower().split(" ")[1:])
    link = music[song]
    webbrowser.open(link)
    if link == "":
        print(f"Sorry, I couldn't find the {song} in your music library.")
        speak(f"Sorry, I couldn't find the {song} in your music library.")