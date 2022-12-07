#!/usr/bin/env python3


import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone(device_index=1)

while True:
    with mic as source:
        try:
            audio = r.listen(source)
            json = r.recognize_google(audio, language="fr-FR")
            print("\njson:\n" +  json)

        except sr.UnknownValueError:
            pass


