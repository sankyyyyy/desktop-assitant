import pyttsx3
import datetime
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.now().hour)
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
        quert = r.recognize_google(audio)
        print(f"User said:{quert}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return quert



if __name__ == "__main__":
    speak("run succesfully")
    takecommand()