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

try:
    with sr.Microphone() as source:
        print('How can I help you?')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'veronica' in command:
            print(command)

except:
    pass

