# Voice recognation


# Write a program to pronounce list of names using win32 API. 
# If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, 
# try to figure out how to do the same thing using some other package


import pyttsx3
names = ["a","b","c","d","e"]
engine = pyttsx3.init()
for name in names:
    engine.say(f"Hellow,I am {name}")
    engine.runAndWait()


# another way 
import win32com.client
namess = ["a","b","c","d","e"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
for name in namess:
    speaker.Speak(f"Hellow,I am {name}")