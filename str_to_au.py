import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

audio = "Hello World"
engine.say(audio)
engine.runAndWait()