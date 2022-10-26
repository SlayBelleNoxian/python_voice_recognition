#!/usr/bin/env python3

#imports
import speech_recognition as sr
import snowboydecoder
import os
import sys
import requests
from gtts import gTTS
#remove erros
#os.close(sys.stderr.fileno())

s = requests.Session()
url = "http://localhost:3000/google/"

#wakeword
def detected_callback():
    print("Detectado!")
    wakeword.terminate()
    recognize()
    wakeword = snowboydecoder.HotwordDetector("Friday.pmdl", sensitivity=0.4, audio_gain=1)
    wakeword.start(detected_callback)

def recognize():
    # obtem o audio do microfone
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        duration = 0.5  # seconds
        freq = 550 # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        print("Say something!")
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            duration = 0.5  # seconds
            freq = 550 # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            t=r.recognize_google(audio, language = "pt-PT");
            print("Google Speech Recognition thinks you said " + t)
            myUrl = url+t;
            try:
                s.get(myUrl)
                print(r.text)
            except: 
                print("Server Down")
                tts = gTTS(text=t, lang='pt-PT')
                tts.save("good.wav")
                os.system("mplayer -speed 1.2  good.wav")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


#wakeword
wakeword = snowboydecoder.HotwordDetector("Friday.pmdl", sensitivity=0.4, audio_gain=1)
#iniciar loop
wakeword.start(detected_callback)
