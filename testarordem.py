#!/usr/bin/env python3

#imports
import speech_recognition as sr
import snowboydecoder
import os
import sys

#remove erros
#os.close(sys.stderr.fileno())


def detected_callback():
    print("Detectado!")
    wakeword.terminate()
     # obtem o audio do microfone
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
        try:
            t=r.recognize_google(audio, language = "pt-PT");
            print("Google Speech Recognition thinks you said " + t)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


#wakeword
wakeword = snowboydecoder.HotwordDetector("snowboy.pmdl", sensitivity=0.5, audio_gain=1)
#iniciar loop
wakeword.start(detected_callback)