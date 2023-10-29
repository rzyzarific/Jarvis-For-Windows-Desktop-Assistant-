import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Zarif!")

    elif hour>=12 and hour<18:
        speak("Good afternoon Zarif!")   

    else:
        speak("Good evening Zarif!")  

    speak("I am on, jarvis mode activated.")       

def take_command():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Kindly Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    take_command()
    while True:
        query=take_command.lower

        #Logic for executing tasks based on query
        if "Saira, open wikipedia" in query:
            speak('Activating Wikipedia...')
            query = query.replace('Wikipedia', '')
            results = wikipedia.summary(query, sentences=2)

