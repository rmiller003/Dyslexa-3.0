# This is a Speech recognition Virtual assistant application using Google AI Voice modules
# Written by Robert Miller in Python 3.9

# pip install pyaudio
# pip install SpeechRecognition
# pip install wikipedia
# pip install pywhatkit
# pip install pyjokes
# pip install pyttsx3
# pip install datetime

import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import pywhatkit
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say('I am your virtual assistant veronica')
engine.say('how can I help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'veronica' in command:
            command = command.replace('veronica', '')
            print(command)

    except:
        pass
    return command

def run_veronica():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


run_veronica()
