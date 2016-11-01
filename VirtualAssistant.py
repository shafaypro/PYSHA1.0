import datetime
import pyttsx
import time  # the time module for the specified intervals
import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
import webbrowser  # Using the web browser , For the browsing purposes
from random import *  # Using the random  function for the creation
import pyaudio  # importing the header file of the pyaudio
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import \
    wikipedia  # using the wikipedia model for accessing the wikipedia and using the modules for the defending purposes.!!
from bs4 import BeautifulSoup  # imporing the beautiful soup package.as

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

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

Search for <--- This opens up the browser for the result so that the Virtual assitant is able to read from the data!!!

Stop,stop listening,quit <---- This will results in the Quiting , exiting for the virtual assistant!!


'''


# The below function will be used regerding to the twitter accessing and stuff
def twitter_access():
    print("Granting the twitter Access")


# The below function will be used for the messaging and getting the messages from the facebook

def messenger_access():
    print("MESSEBGER ACCESS FOR SENDING AND RECIEVING MESSSAGES")

# The below function will be used to access the facebook and all the stuff.
def facebook_access():
    print("FACEBOOK Access for accessing and recieving facebook messages")


# This will be used to access the instagram, so that you can access the current features
def instagram_access():
    print("Granting the instagram Access and checking")

# This function will be used to access the social medias and choose the correct social media for the particular stuff.


def social_media_access():
    print("")


# The Below function will be used to search on the browser and then show the desire result
def search_browser(text_input):
    print('-This is for the searching on browser-')
    try:
        url = 'http://google.com/search?q=' + text_input  # Creating or generating a google link for the particular file
        webbrowser.open(url)
        return

    except:
        text_to_speech(
            "I'm sorry, I couldn't reach google")  # Calling the Function so that it can be identified that ,machine can speaks for itself
        return


# The below function is responsible for the search on the wikipedia.

# searching on the wikipedia and then asking the pysha to speak the respectable result!!


def search_wikipedia(text_input):
    suggested_text = text_input.strip()  # strips the extra white space
    print(suggested_text)
    # suggested_string = wikipedia.suggest(suggested_text)  # now going for the suggestion
    try:
        wiki_page = wikipedia.page(suggested_text)  # this opens up the wiki page for the particular thing
        # text_to_speech(str(wiki_page.title))  # asking the machine to speak this specified word
        # summary_text = wikipedia.summary(suggested_text, sentences=4)  # search on the wikipedia!
        wiki_link = str(wiki_page.url)  # Converts the url of the wiki links to the url.
        wiki_images = wiki_page.images  # Gets all the images link references. as a list
        webbrowser.open(wiki_link)  # opens the link on the web browser and then search the specified text link
        text_to_speech(wikipedia.summary(suggested_text, sentences=3))
        return
    except:
        text_to_speech(
            "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem")
        return


# The below function is responsible for the running of the chat with the below function


def chat(input):
    insults = ["weirdo", "stupid", "weird", "dumb", "idiot", "retard", "retarded", "fat", "lazy",
               "annoying", "moron", "simp", "big", "ugly", "sad", "wimp", "troll"]
    complements = ["nice", "happy", "good", "smart", "wonderful", "really ", "intellegent", "awesome", "beautiful"]
    ranNum = randrange(1, 4)
    # chatting features of PyDa:
    if input.startswith("do you want to "):
        if ranNum == 1:
            text_to_speech("Maybe later")
        if ranNum == 2:
            text_to_speech("I don't think that's a good idea")
        if ranNum == 3:
            text_to_speech("Yes! lets do it")

    if input.startswith("do you like to "):
        if ranNum == 1:
            text_to_speech("Sometimes I do")
        if ranNum == 2:
            text_to_speech("No, I hate doing that")
        if ranNum == 3:
            text_to_speech("Yes, I do that all the time")

    if input.startswith("i hate "):
        if "Shafay" in input[6:]:
            text_to_speech("What? Shafay is the coolest person ever!")
        elif ranNum > 2:
            text_to_speech("I think " + input[6:] + " is awesome")
        elif ranNum <= 2:
            text_to_speech("I don't like " + input[6:] + ' either')

    words = input.split

    if input.startswith("you are a"):
        if any(input[10:].startswith(c) for c in complements):
            if ranNum == 1:
                text_to_speech("Thank you, I know")
            if ranNum == 2:
                text_to_speech("isn't it obvious?")
            if ranNum == 3:
                text_to_speech("you made my day!")
        elif any(input[11:].startswith(c) for c in complements):
            if ranNum == 1:
                text_to_speech("Thank you, I know")
            if ranNum == 2:
                text_to_speech("isn't it obvious?")
            if ranNum == 3:
                text_to_speech("you made my day!")

        if any(input[10:].startswith(i) for i in insults):
            if ranNum == 1:
                text_to_speech("I know you are but what am i?")
            if ranNum == 2:
                text_to_speech("Don't troll me. bad things will happen")
            if ranNum == 3:
                text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")
        elif any(input[11:].startswith(i) for i in insults):
            if ranNum == 1:
                text_to_speech("I know you are but what am i?")
            if ranNum == 2:
                text_to_speech("Don't troll me. bad things will happen")
            if ranNum == 3:
                text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")

        elif input[10:] or input[11:] not in insults:
            if ranNum == 1:
                text_to_speech("I don't know what you mean by that")
            if ranNum == 2:
                text_to_speech("Your words are not in my library")
            if ranNum == 3:
                text_to_speech("No comment")
        elif input[10:] or input[11:] not in complements:
            if ranNum == 1:
                text_to_speech("I don't know what you mean by that")
            if ranNum == 2:
                text_to_speech("Your words are not in my library")
            if ranNum == 3:
                text_to_speech("No comment")

    if input.startswith("are you a"):
        if any(input[10:].startswith(c) for c in complements):
            if ranNum == 1:
                text_to_speech("yes i am")
            if ranNum == 2:
                text_to_speech("isn't it obvious?")
            if ranNum == 3:
                text_to_speech("you betcha")
        elif any(input[11:].startswith(c) for c in complements):
            if ranNum == 1:
                text_to_speech("yes i am")
            if ranNum == 2:
                text_to_speech("isn't it obvious?")
            if ranNum == 3:
                text_to_speech("you betcha")

        if any(input[10:].startswith(i) for i in insults):
            if ranNum == 1:
                text_to_speech("no, are you")
            if ranNum == 2:
                text_to_speech("don't troll me, i eat trolls")
            if ranNum == 3:
                text_to_speech("does it look like i am?")
        elif any(input[11:].startswith(i) for i in insults):
            if ranNum == 1:
                text_to_speech("no, are you")
            if ranNum == 2:
                text_to_speech("don't troll me, i eat trolls")
            if ranNum == 3:
                text_to_speech("does it look like i am?")

        elif input[10:] or input[11:] not in insults or complements:
            if ranNum == 1:
                text_to_speech("I don't know what you mean by that")
            if ranNum == 2:
                text_to_speech("Your words are not in my library")
            if ranNum == 3:
                text_to_speech("No comment")


# if there is any person question regerding to the Virtual Assistant go for this


def Personal_PYSHA(text_input=""):
    text_input = text_input.strip()  # striping the extra white spaces.
    if text_input == "name":
        text_to_speech("PYSHA")
        return
    elif text_input == "age":
        b_date = datetime.date(2016, 10, 24)  # specifing the creation date.
        c_date = datetime.date.today()
        # now subtract the date from the date of creation
        text_to_speech((c_date - b_date))  # this prints the age of the Virtual Assistant , which returns the date.
        print((c_date - b_date))
        return
        # Here you need to add the hob
    elif text_input == "hobbies":
        text_to_speech("Well i have many hobbies, i will tell you some")
        hobbies = ["Playing a Game", "Collecting your History", "Watching Football"]
        for each_hobby in hobbies:  # Iterating to each of the loops
            text_to_speech(str(each_hobby))  # Sending the each string to the Hobbies.
            # This will send all the related hobbies to the specified Place.
    elif text_input == "gender":
        text_to_speech("Female")


def day_check():
    current_date = datetime.datetime.now()
    text_to_speech("The current date is " + str(current_date.date()))
    return


# Checking the time for the computer while the


def time_check():
    current_time = time.strftime('%H:%M:%S')
    text_to_speech("The time is " + current_time)
    return


# storing the respectable input for the user  while the computer will be able to use the resources and speak


def store_userinput(input_check):
    file_out = open("USERINPUT.txt", "a")
    file_out.writelines("USER SAID: \t" + input_check)
    file_out.write("\n")  # ending the line with the next line
    file_out.close()
    return
    # This function will be responsible for storing the responses so that it may able to answer in the future.pute


# Converting the spoken string to the speech , so that the call is Visible


def speech_to_Text():
    client_id = ""  # this is the google api client id
    client_secret = ""  # this is the google api client secret key
    api_key = ""
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


# if you want to record for the specific interval of time


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


#
# Converting the text to speech using the pysha personal assistant and then specifing the input!


def text_to_speech(text_input='HI! my name is PYSHA and i am your assistant'):
    engine = pyttsx.init()
    engine.say(text_input)
    engine.runAndWait()
    return


# Checking the input of the speech to text so that the result can cbe picked up and then stored in the displat ..!!!


def speech_to_text_wav(file_to_recognize):
    r = sr.Recognizer()

    with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file

    try:

        total_saying = r.recognize_google(audio)
        print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
        # here i will be working on latter analysis
        total_saying = str(total_saying).lower()  # converting the total saying to the strings
        process_text_input(total_saying)

    except LookupError:  # speech is unintelligible
        print("Could not understand audio")
    except sr.UnknownValueError:
        print("UNKNOWN!!")


# The follwing function will be responsible for the text to be parsed regerding to the certain input.

# keep in mind to use the natural language processing ,, www.pythonprogramming.org


def process_text_input(total_saying=""):
    if (total_saying.strip()).lower() == "quit" or (
            total_saying.strip()).lower() == "stop listening" or total_saying.strip().lower() == 'stop':
        text_to_speech("Bye! my friend")
        exit()  # exiting the program
    else:
        # this stores the Specified Input we said Regerding to something
        # Textual_Analysis(total_saying)
        '''
            Below is the place where are your working on!!!

            '''
        if (total_saying.lower()).startswith('search for'):
            text_to_speech("Opening a Browser For you.")
            store_userinput("Searching on Browser :" + total_saying[10:])
            search_browser(
                text_input=total_saying[10:])  # sending every remanining thing to the Browser to browse for

        elif total_saying.lower().__contains__('on wikipedia') and total_saying.startswith('search'):
            total_saying = total_saying.lower()  # this converts the string to the lower case
            total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
            total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
            text_to_speech("Searching on WIkipedia..")
            search_wikipedia(total_saying)  # calling the wikipedia search function , for the results

        elif total_saying.lower().startswith("what is the date") or total_saying.lower() == 'date':
            # Here you will be required to input the date
            day_check()  # This calls the day check
        elif total_saying.lower().startswith("what is the time") or total_saying.lower() == 'time':
            time_check()  # this checks the current time according to the specified state

        # Create a Grammer , that represents the questions regerding to the respectable machine
        elif total_saying.lower().startswith("what is your"):
            # here you need to create the question saying file so that the file is readable.
            '''
                Write the Respectable question in this format so that, the Agent learns from the file.

                '''
            total_saying = total_saying.replace("what is your",
                                                "")  # replacing the words so that it will be easier for the program to Check the last thing
            Personal_PYSHA(total_saying)
        else:
            chat(total_saying)
            # .###.....


def main():
    print("--")
    # duration = float(input("How much time you need to record for ?"))
    # record_something(duration)  just trying to pause the thing
    client_id = ""  # this is the google api client id
    client_secret = ""  # this is the google api client secret key
    text_to_speech()  # Calls the virtual assistant to speech
    # speech_to_Text()  # calling the function
    while True:
        record_something(7)
        speech_to_text_wav("output.wav")


if __name__ == '__main__':
    main()  # Calling the main Function .!!
# The above the Audio has been recorded , and now the Audio needs to be converted into texts/
