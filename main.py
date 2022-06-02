import speech_recognition as sr  # pip install speechRecognition
import pyautogui
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

def notepad():
    pyautogui.press('win', interval=0.2)
    pyautogui.typewrite('notepad', interval=0.2)
    pyautogui.press('enter', interval=0.2)

def speech():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1

        audio_data = r.record (source,duration=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio_data, language='en-in')
        pyautogui.typewrite(query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
        notepad()
        while True:
          speech()




