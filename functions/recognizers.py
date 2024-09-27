
import speech_recognition as sr
import os
import sys
import pyttsx3
from pyttsx3.drivers import NassSpeechDriver
from objc import objc  # <--- Add this line to import objc

def install_portaudio():
    if os.name == 'posix':
        os.system('brew reinstall portaudio')
    elif os.name == 'nt':
        os.system('pip install pyaudio')
    else:
        os.system('sudo apt-get install libportaudio2')

def install_pyaudio():
    try:
        import pyaudio
    except ImportError:
        if os.name == 'nt':
            os.system('pip install pyaudio')
        else:
            os.system('sudo pip install pyaudio')
        print("PyAudio installed. Please run the program again.")
        sys.exit(0)

def install_distutils():
    try:
        import distutils
    except ImportError:
        if os.name == 'posix':
            os.system('python -m ensurepip --upgrade')
            os.system('pip install --upgrade setuptools')
        elif os.name == 'nt':
            os.system('pip install --upgrade setuptools')
        else:
            os.system('sudo apt-get install python3-distutils')
        print("Distutils installed. Please run the program again.")
        sys.exit(0)

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand your audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

install_portaudio()
install_pyaudio()
install_distutils()

# Example usage:
# text = speech_to_text()
# if text:
#     text_to_speech(text)

text_to_speech("this is test")
