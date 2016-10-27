import pyttsx


def speak(message=""):
    engine = pyttsx.init()  # intializing the Engine for speaking
    engine.say(message)
    engine.runAndWait()  # This will run the engine and the engine will wait for it
