import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function for live voice transcription
def live_transcription():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source, phrase_time_limit=1.3)  # Adjust the phrase time limit as needed
                text = recognizer.recognize_google(audio)  # Using Google's Speech Recognition API
                print("Transcription:", text)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call live transcription function
live_transcription()
