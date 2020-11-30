import os
import time
import speech_recognition as sr
from win32com.client import Dispatch

s = Dispatch("SAPI.SpVoice")

def speak(text):
	s.Speak(text)

pngs = [x for x in os.listdir() if x.endswith(".PNG")]
name = [x.split(".")[0] for x in os.listdir() if x.endswith(".PNG")]

for n in range(1):
    for j in range(1,4):
            r = sr.Recognizer()
            with sr.Microphone() as source:

                print ('Say Something!')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print(text)
                    speak(text)
                except:
                    print('Did not get that try Again')
                    text=''
    time.sleep(1)
