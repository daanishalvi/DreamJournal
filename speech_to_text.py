import speech_recognition as sr


#read duration from the arguments
duration = 7

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:

    

    try:
    # read the audio data from the default microphone
        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)


    except sr.UnknownValueError:
        print("Could not understand")