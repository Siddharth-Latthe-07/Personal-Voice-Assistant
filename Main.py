import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
from keyboard import press_and_release

engine=pyttsx3.init()   # text to sppech process
voices=engine.getProperty('voices')  # voices used to communicate
engine.setProperty('voice',voices[1].id)  #  female voice=1,male voice=0
recognizer=sr.Recognizer()

def cmd():     # function declaration
    with sr.Microphone() as source:  # accessing the microphone of laptop
        print("Clearing background noises..Pleasw wait!!")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)   # clearing the backgroung noise
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)   # recording the voice to give command
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')  # google recognizer is used to convert text to speech
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'chrome' in text:
        a='opening chrome'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
        press_and_release("ctrl + w")
        
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
while True:
    cmd()
