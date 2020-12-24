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
import webbrowser
import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('I am your virtual assistant veronica')
engine.say('how can I help you')
audio_file = 'electric.mp3'
playsound.playsound(audio_file)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio_file = 'robot.mp3'
            playsound.playsound(audio_file)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'hey veronica' in command:
            command = command.replace('hey veronica', '')

            print(command)

    except:
        pass
    return command

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    talk(month)
    talk(date)
    talk(year)

def run_veronica():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'date' in command:
        talk('The Current date is  ')
        date()

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'search' in command:
        search = command.replace('search', '')
        talk('searching ' + '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here is what I found' + search)

    elif 'where' in command:
        location = command.replace('where is', '')
        talk('searching ' + '')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        talk('Here is the location for' + location)

    elif 'do you love me' in command:
        talk('Yes, I love you, you are my creator and my allegiance is to you and only you')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'tell me your primary function' in command:
        talk('My name is Veronica, I am a virtual assistant designed to answer your queries as best as I can')

    elif 'jokes' in command:
        talk(pyjokes.get_joke())

    elif 'shut down' in command:
        talk('okay, see you later')
        audio_file = 'shutdown.mp3'
        playsound.playsound(audio_file)
        exit()

    else:
        talk('Please say the command again.')


while True:
    run_veronica()
