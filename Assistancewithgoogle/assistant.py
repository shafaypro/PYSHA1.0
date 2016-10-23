import speech_recognition as sr
import webbrowser
import pyttsx
import time

eng = pyttsx.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)


while True:

    r = sr.Recognizer()
    mw = 'search for'
    slst = 'stop listening'

    with sr.Microphone() as source:

        audio = r.listen(source, timeout = None)

        try:

            if mw in r.recognize_google(audio):

                r2 = sr.Recognizer()

                print('What am I searching for?')
                eng.say('What am I searching for?')
                eng.runAndWait()

                with sr.Microphone() as source2:

                    audio2 = r2.listen(source2)

                try:

                    text=r2.recognize_google(audio2)
                    print("Your query: " + r2.recognize_google(audio2))
                    eng.say('I am looking for:  ')

                    eng.say(r2.recognize_google(audio2))
                    eng.runAndWait()
                    url='http://google.com/search?q='+r2.recognize_google(audio2)
                    webbrowser.open(url)

                except sr.UnknownValueError:
                    eng.say("I'm sorry, I couldn't understand you")
                    eng.runAndWait()
                    print("I'm sorry, I couldn't understand you")

                except sr.RequestError:
                    eng.say("I'm sorry, I couldn't reach google")
                    eng.runAndWait()
                    print("I'm sorry, I couldn't reach google")

            elif slst in r.recognize_google(audio):

                eng.say("Shutting down")
                eng.runAndWait()
                print("Shutting down...")
                break

        except sr.UnknownValueError:
            print("Listening to the magic words: 'search for' or 'stop listening'")

        except sr.RequestError:
            eng.say("I'm sorry, I couldn't reach google")
            eng.runAndWait()
            print("I'm sorry, I couldn't reach google")