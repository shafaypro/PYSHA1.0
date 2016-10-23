import pyaudio  # importing the header file of the pyaudio
import wave  # Importing the wave of for the recording(This isthe format for the recording which is used .wav
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import pyttsx
import numpy
import pandas
import time
import os
import nltk  # for the natural language processing later on

def PYSHA_QUESTIONS():
    print("")
    # here Pysha Will be able to ask the question based in particular things on common.

def store_responce():
    print("")
    # This function will be responsible for storing the responses so that it may able to answer in the future.

def speech_to_Text():
    client_id = "637371925027-ia8s5a41fialrb0hcjlaoq4gaa41d38o.apps.googleusercontent.com"  # this is the google api client id
    client_secret = "-KyaxAejOWUzvyGUn-PtcCnd"  # this is the google api client secret key
    api_key = "AIzaSyBRkgyt05ybcRG3Jogp7sIts0jcxPqi7TY"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
        CHANNELS = 2  # The Cross Channels
        # RATE = 44100
        source.CHUNK = CHUNK
        source.format = FORMAT
        # print(dir(source))
        print("Say something!")
        print(r.energy_threshold)
        r.energy_threshold -= 80
        # print(r.adjust_for_ambient_noise(source,duration=1))
        audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        # print(r.energy_threshold )
        # print(help(r.recognize_google))
        print("You said: " + r.recognize_google(audio, language='en-US'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def record_something(duration):
    # Below the Audio is accessed and then the audio is recorded and then converted in to text
    CHUNK = 1024  # Specifying the chunks for the recording
    FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
    CHANNELS = 2  # The Cross Channels
    RATE = 44100  # Bit rate , at which to record
    RECORD_SECONDS = duration  # Recording time duration for the computer
    WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name as a string

    p = pyaudio.PyAudio()  # creating the Object and then calling the function of the PyAudio to access the audio

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # Creating the stream and specifing the access channels , and the rate, Input to be on.

    print("* recording, Ask me something!")  # Just a Message to tell the user that the Voice is being recorded

    frames = []  # A list of frame is created which is

    for i in range(0, int(
                            RATE / CHUNK * RECORD_SECONDS)):  # This is the Rate(bit rate) / Chuncks to be recorded * the Seconds
        data = stream.read(CHUNK)  # Reading the dat afrom the stream
        frames.append(data)  # Adding the each data to the frame list and appending it up.

    print("* done recording")

    stream.stop_stream()  # Stopping the stream so that the stream(recorder for audio is stopped )
    stream.close()  # Clossing the stream of the audio
    p.terminate()  # Termination the Py AUDIO Module cause it was accessedd

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # Accessing the WAV
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def Text_to_speech():
    engine = pyttsx.init()
    engine.say('HI! my name is Shafay2 and i am your virtual assistant')
    engine.runAndWait()


def speech_to_text_wav(file_to_recognize):
    r = sr.Recognizer()
    with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file

    try:
        total_saying = r.recognize_google(audio)
        print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
        # here i will be working on latter analysis
        total_saying = str(total_saying)  # converting the total saying to the strings

        if total_saying == "quit":
            exit()  # exiting the program
    except LookupError:  # speech is unintelligible
        print("Could not understand audio")


def main():
    print("--")
    # duration = float(input("How much time you need to record for ?"))
    # record_something(duration)  just trying to pause the thing
    client_id = "637371925027-ia8s5a41fialrb0hcjlaoq4gaa41d38o.apps.googleusercontent.com"  # this is the google api client id
    client_secret = "-KyaxAejOWUzvyGUn-PtcCnd"  # this is the google api client secret key
    Text_to_speech()  # Calls the virtual assistant to speech
    speech_to_Text()  # calling the function
    #record_something(10)
    speech_to_text_wav("output.wav")


if __name__ == '__main__':
    main()  # Calling the main Function .!!
# The above the Audio has been recorded , and now the Audio needs to be converted into texts/
