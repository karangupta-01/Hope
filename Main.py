from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pywhatkit
import sys
engine = pyttsx3.init('sapi5')
pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak(" i am hope, an artificial intiligence.")

def takecommand():
    '''it takes microphone input from the user and return string inputs'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Just wait a second......")
        speak("Just wait a second......")
        query = r.recognize_google(audio, language='en-in')
        print(f"Master Said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

wishme()

if __name__ == "__main__":
    while(True):
        query = takecommand().lower()
        if 'search' in query:
            try:
                speak("Searching wikipedia.....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("An Error Occured!")
                speak("An Error Occured!")
        elif "exit" in query:
            speak("Good bye master!")
            sys.exit()
        elif "open youtube" in query:
            speak("What should I play on Youtube?")
            a = takecommand().lower()
            print(f"User said:{a}")
            pywhatkit.playonyt(f"{a}")
        elif "open google" in query:
            speak("What should I search on Google?")
            b = takecommand().lower()
            print(f"User said:{b}")
            pywhatkit.search(f"{b}")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir the time is{strTime}")
        elif "open chrome" in query:
            os.system("start chrome")
        elif "open github" in query:
             webbrowser.open("https://github.com/")
        elif "open cmd" in query:
             os.system("start cmd")
        else:
            speak(f"Would you like me to search {query} on google?")
            z = takecommand().lower()
            if "yes" in z:
                try:
                    speak("Searching.....")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    print("No result found!")
                    speak("No result found!")
            elif "no" in z:
                print("Ok")
                speak("Ok")