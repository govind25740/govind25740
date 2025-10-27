import pyttsx3
import speech_recognition as sr
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make Jarvis speak."""
    engine.say(text)
    engine.runAndWait()

def wish_user():
    """Function to greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I assist you?")

def take_command():
    """Function to take voice input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"
        return query

if __name__ == "__main__":
    wish_user()
    while True:
        command = take_command().lower()
        if command == "None":
            continue
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
        elif "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I am sorry, I can only tell the time or exit for now.")


            
   




