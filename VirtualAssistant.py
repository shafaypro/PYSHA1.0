import pyaudio  # importing the header file of the pyaudio
import wave  # Importing the wave of for the recording(This isthe format for the recording which is used .wav
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import pyttsx
import time
import os
import datetime
import tkinter # This is later for the GUI purposes


'''
// This build is heavily under progress by Muhammad Shafay Amjad, If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/VirtualAssistant
Info Dated: 24/10/2016

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formated as WAV, under the FLAC encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the string

'''


def day_check():
    current_date = datetime.datetime.now()
    full_date = str(current_date.day) + ' ' + time.strftime('%A') + ' ' + time.strftime('%B')
    Text_to_speech("The current date is " + full_date)
    return


def time_check():
    print('')
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%x')
    full_date = time.strftime('%A') + ' ' + time.strftime('%B')
    Text_to_speech("The date is " + full_date)
    return


def stored_answers():
    print("--")
    return
    # This will have the already stored items


def PYSHA_QUESTIONS():
    print("")
    return
    # here Pysha Will be able to ask the question based in particular things on common.


def store_userinput(input_check):
    file_out = open("USERINPUT.txt", "a")
    file_out.writelines("USER SAID: \t" + input_check)
    file_out.write("\n")  # ending the line with the next line
    file_out.close()
    return
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


def Text_to_speech(input='HI! my name is PYSHA and i am your assistant'):
    engine = pyttsx.init()
    engine.say(input)
    engine.runAndWait()
    return


def Textual_Analysis(Inp_MSG='NONE'):
    Inp_MSG = Inp_MSG.strip()  # stripping for the extra white spaces
    if Inp_MSG.__contains__("current time"):
        print("")


def speech_to_text_wav(file_to_recognize):
    r = sr.Recognizer()
    with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file

    try:
        total_saying = r.recognize_google(audio)
        print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
        # here i will be working on latter analysis
        total_saying = str(total_saying)  # converting the total saying to the strings
        # store_userinput(total_saying)
        if (total_saying.strip()).lower() == "quit":
            exit()  # exiting the program
        else:
            store_userinput(total_saying)  # this stores the Specified Input we said Regerding to something
            Textual_Analysis(total_saying)
    except LookupError:  # speech is unintelligible
        print("Could not understand audio")


def main():
    print("--")
    # duration = float(input("How much time you need to record for ?"))
    # record_something(duration)  just trying to pause the thing
    client_id = "637371925027-ia8s5a41fialrb0hcjlaoq4gaa41d38o.apps.googleusercontent.com"  # this is the google api client id
    client_secret = "-KyaxAejOWUzvyGUn-PtcCnd"  # this is the google api client secret key
    Text_to_speech()  # Calls the virtual assistant to speech
    # speech_to_Text()  # calling the function
    while (True):
        record_something(10)
        speech_to_text_wav("output.wav")


if __name__ == '__main__':
    main()  # Calling the main Function .!!
# The above the Audio has been recorded , and now the Audio needs to be converted into texts/
