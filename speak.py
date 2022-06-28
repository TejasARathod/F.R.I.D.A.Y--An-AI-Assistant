import pyttsx3


def speak(audio):  # function for our AI to speak 
    engine = pyttsx3.init('sapi5') # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft
    voices = engine.getProperty('voices') # Gets the current value of a property ; voices: List of L{voice.Voice} objects supported by the driver
    engine.setProperty('voice',voices[2].id) # Adds a property value to set to the event queue
    engine.say(audio) # say: Adds an utterance to speak to the event queue  ; the engine will speak up the text 
    engine.runAndWait() # Runs an event loop until all commands queued up until this method call complete. Blocks during the event loop and returns when the queue is cleared.

