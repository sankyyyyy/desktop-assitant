import pyttsx3
import datetime
#from datetime import*
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
from random import*

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning")
    elif hour >= 12 and hour <=18:
        speak("Good afternoon")
    else:
        speak("Good night")


def takecommand():
    ''' it takes microphone inputs of the user and returns screenoutput'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    #speak("run succesfully")
    query= takecommand().lower()
    #logic for executing task
    if 'wikipedia' in query:
        try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        except Exception as e:
            #print(e)
            print("Result not found!")
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open github' in query:
        webbrowser.open("github.com")

    elif 'play music' in query:
        music_dir = "D:\\2\\songs"
        #set path of your desktop for songs
        random_index = randint(1,100)
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[random_index]))
    
    elif 'time' in query:
        strTime = datetime.datetime.now()
        strTime.strftime("%H-%M")
        print(strTime)
        speak(f"Sir,the time is{strTime}")

    elif 'open code' in query:
        #set your path here in codePath
        codePath = "C:\\Users\\sanke\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

