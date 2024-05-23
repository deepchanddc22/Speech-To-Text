import speech_recognition as sr
from time import sleep

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to handle speech
def handle_speech(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)  # Using Google's Speech Recognition API
        print("Transcription:", text)
    except sr.UnknownValueError:
        pass  # Ignore if speech is not recognized
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Function for live voice transcription
def live_transcription():
    print("Listening...")

    stop_listening = recognizer.listen_in_background(sr.Microphone(), handle_speech)

    # Keep running indefinitely
    try:
        while True:
            sleep(0.001)  # Check every 0.1 seconds
    except KeyboardInterrupt:
        # Stop the background listening process upon keyboard interrupt
        stop_listening(wait_for_stop=False)

# Call live transcription function
live_transcription()
