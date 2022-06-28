import speech_recognition as sr # Library for performing speech recognition, with support for several engines and APIs, online and offline


def listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer() # this class will help us recognize the audio
    with sr.Microphone() as source: # Creates a new ``Microphone`` instance, which represents a physical microphone on the computer
        print('Listening...')
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source,0,5) # Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance, which it returns.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None" 

    query = str(query)
    return query.lower()