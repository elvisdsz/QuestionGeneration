import os
import speech_recognition as sr
from tkinter.filedialog import askopenfilename

def convertToMP3(filename):
   command = "ffmpeg -i "+filename+".mp4 "+filename+".mp3"
   os.system(command)

def convertToWAV(filename):
   commandwav = "ffmpeg -i "+filename+".mp3 "+filename+".wav"
   os.system(commandwav)

def audioToText(filename):
   AUDIO_FILE = "video.wav"
   r = sr.Recognizer()
   audioFile = sr.AudioFile(AUDIO_FILE)

   with audioFile as source:
      audio = r.record(source, duration=100)

   print(type(audio))
   print("------------------------------------")
   text = r.recognize_google(audio)
   #text = r.recognize_sphinx(audio)
   print(text)

   
filename = askopenfilename(filetypes=[("*","*.mp4")]) # queryImage
temp = os.path.splitext(filename)
convertToMP3(temp[0])
convertToWAV(temp[0])
audioToText(temp[0])

