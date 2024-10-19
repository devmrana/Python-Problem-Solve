import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  
text = "We have used the Google API, but what if we want to convert text to speech using offline. Python provides the pyttsx3 library, which looks for TTS engines pre-installed in our platform."  
engine.say(text)  
# play the speech  
engine.runAndWait()