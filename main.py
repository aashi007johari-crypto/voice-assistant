import speech_recognition as sr
import webbrowser 
import pyttsx3
import time
import musicLibrary
import requests
import feedparser 



def speak(text):
    engine=pyttsx3.init()

    engine.say(text)
    engine.runAndWait()

from openai import OpenAI

def aiProcess(command):
    client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key="b3d6302d-03cf-4b68-96d8-4a4d84b3424a"
    )

    completion = client.chat.completions.create(
        model="Meta-Llama-3.3-70B-Instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.Give summary and short Responses please" 
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "famous influencer" in c.lower():
        webbrowser.open("https://www.instagram.com/glam.ashh?igsh=bHB4c2h2a250cHhh")
    elif  "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
      try:
        song = c.lower().replace("play","").strip()
        
        if song:
           speak(f"Playing {song}")
           search_url= f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
           webbrowser.open(search_url)

        else:
            speak("Please tell me the song name")
      except:
        speak("song not found")
        
        
    elif "news" in c.lower():
       speak("here are the latest news")
       feed=feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
       for entry in feed.entries [:5]:
           speak(entry.title)
    else:
        output = aiProcess(c)
        speak(output)
        
      

if __name__ == "__main__":
    speak("Initiallizing Jarvis....")
    r = sr.Recognizer()
    while True:
        #listen for the wake woed jarvis

       
        # recognize speech using google
        try:
            with sr.Microphone() as source:
              print("Listening.....")
              audio = r.listen(source,timeout=5,phrase_time_limit=3)

            word = r.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                time.sleep(1) 

                speak("yes")   
               
                #Listen for command
                with sr.Microphone() as source:
                  print("Jarvis Active..")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  print(command)
                  processCommand(command)
                  
    
        except Exception as e:
            print("error :", e)
