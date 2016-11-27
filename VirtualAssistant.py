import datetime
import os
import pyttsx  # Python text to speech and speech to text
import time  # the time module for the specified intervals
import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
import webbrowser  # Using the web browser , For the browsing purposes
from random import *  # Using the random  function for the creation
from tkinter import *  # For the GUI Tkinter package
import pyaudio  # importing the header file of the pyaudio
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import wikipedia  # using the wikipedia model
from bs4 import BeautifulSoup  # beautiful soup
import urllib  # For the scrapping of the urllib
import threading  # for multiple threading
import nltk # For natural languagae processing

'''
// This build is heavily under progress by Muhammad Shafay Amjad, If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/VirtualAssistant
Info Dated: 24/10/2016

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formatted as WAV, under the F.L.A.C encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

Search for <--- This opens up the browser for the result so that the Virtual assitant is able to read from the data!!!

Stop,stop listening,quit <---- This will results in the Quiting , exiting for the virtual assistant!!

search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)

what is the ----> Time, Date and others can tell you the the time ,date and others.
Ther are some other features also added in the header file , like haviing a random chat and working on different kind of
Loops
'''

''' Keep in mind to have all the back up things,
For the personal computer you need to have the computer access,
And all the other things given to the Assistant so that it can work in there.
'''
__author__ = "M Shafay Amjad"
__QA__ = "mshafayamjad@gmail.com"

# The reverse shell process is for personal use, where we will be using to ping the Updated Code, to your Home location
# Computer Code!
class Reverse_Shell:
    def __init__ (self):
        print("Contacting the Home Server ( Reverse shell) ")

    def connect (self):
        print("connecting to the home server!!!")


# This Joke Class is created By Muhammad Shafay Amjad for the showing of the comic and comic from the internet
'''
    The joke class was created by M Shafay Amjad ,for the purpose of building the Joke Regerding to the Specified Things or categories ,
    Since the Joke class also has the ability to show a comic , while search for a random Joke even , It has also the ability to search for a particular thing.
'''


class Joke(object):
    def __init__ (self, input_text=""):
        print("")
        self.input_text = input_text

    def random_joke (self):
        joke_number = random.randint(0, 500)
        joke_web_api_link = "http://api.icndb.com/jokes/" + str(joke_number)
        print(joke_number)

    '''
        A Basic module for the scraping for the comic images from the website for the python module.!
    '''

    def Image_Commic (self):
        comic_number = random.randint(0, 1000)
        print(comic_number)
        scraped_page = urllib.request.urlopen("https://xkcd.com/" + str(
            comic_number))  # This opens up the link which need to be scrapped according to the number
        html_data = scraped_page.read()
        soupified_page = BeautifulSoup(html_data, "html.parser")  # Specifying the way, which to parse the page !
        # print(soupified_page.prettify()) # This is just for the debugging purposes for the generation of the sopified page
        comic_image_link = soupified_page.find('div', {
            'id': 'comic'})  # this search for the div tag wit hteh attribute of the id class and the comic , Named id
        # print(comic_image_link.img["src"])
        source = "http://" + comic_image_link.img["src"][
                             2:]  # getting the source from the image link then passing to the show Image function:
        picture_file_name = os.getcwd() + '\\C_Images\\' + str(comic_number) + source[-4:]
        # print(picture_file_name)  just for the debugging purposes
        downloaded_image = urllib.request.urlretrieve(source, picture_file_name)
        # print(downloaded_image)
        self.show_image(picture_file_name)  # Passing the Picture file name to the specified image  to the function
        # self.show_image(source.strip()[2:])

    def show_image (self, location='', label_text=''):
        if location == '':
            root = Tk()  # Creating a root element using the Tkinter module Tk()
            label1 = Label(root, text=label_text, font='size,20')  # This is the label insertion for the Tkinter module
            print(label1)  # Showing in the console for the debuggin purposes
            label1.pack()  # Packing up the label1 module in the GUI
            root.mainloop()  # Executing the main loop for the Gui Till it gets exited
            # print("")
        else:
            root = Tk()  # Creating a root element for the tkinter
            photo = PhotoImage(file=location)
            Label_img = Label(root, image=photo)
            Label_img.pack()  # This packs this image in the Loop
            root.mainloop()  # run the loop to show the gui image for the specified !

    # There are some certain sites for the scrapping for the particular page and an api , which is
    # http://api.icndb.com/jokes/random/
    def joke_about (self, about=""):
        print("Under Construction!")

    def joke_category (self, category=["nerdy,explicit"]):
        # print("this is the Joke Category list which will scrap the site and provide the Joke regerding to the Category")
        joke_web_api_link = "http://api.icndb.com/jokes/random?limitTo=[" + str(
            category) + "]"  # Limiting the link with the specification for the particular category !
        scrapped_page = str(urllib.request.urlopen(
            joke_web_api_link).read())  # Reading all the requested Scrapped Page from the Api , to see the page .
        # print(scrapped_page[:])
        # Its need a fixing script here that would parse the json unformed file .!
        joke_start = scrapped_page.find('"joke": ') + 9
        joke_end = scrapped_page[joke_start:].find('"categories"')
        joke_text = scrapped_page[joke_start:joke_start + joke_end]
        return joke_text
        # self.show_image('',joke_text)

    def Image_Joke (self):
        self.Image_Commic()
        #pass


# This function will tell the current weather for the Specified City , Other wise the default weather for the current city
# Using the Open weather Map for the getting the temprature for the current weather
# references are from open weather map , which is doing all the performance stuff.
class weather_checking:
    def __init__ (self):
        print("Weather Checking Class initialized !")

    def weather_check (text_input=""):
        print(
            'This function will be responsible for telling the current weather for the particular city or Longitude and latitude.')


# going in the form of the chat bot, since the particular chat bot will be used
class TextMode:
    def __init__(self):
        print("text mode Class Accessed!")
    def text_mode(self,text_input=''):
        print("--runs the Text Mode --")
    # here you need tohave a user interface , and then provide a chatting history to!



# This will be used to launch the applications

'''
Comic and Jokes will be dealt with in the below Parts.

'''


# Reminders, this function will be used to remind you about things.
class Reminders:
    def __init__(self):
        print("Reminders Class Created !")

    def reminders_access (self, date=''):
        """

        :param date:
        """
        print(date)


# keep in mind that it can also be used for the other queries like loggin into the particular websites.
# These all moduels are under progress,
# Development module will be started building after 30 november 2016, !
class SocialMedia:
    def __int__ (self):
        print("This is the Constructor of the class Social media")

    def email_access (self):
        print("")

    # The below function will be used regerding to the twitter accessing and stuff
    def twitter_access (self):
        print("Granting the twitter Access")

    # The below function will be used for the messaging and getting the messages from the facebook

    def Messenger_access (self):
        print("MESSEBGER ACCESS FOR SENDING AND RECIEVING MESSSAGES")

    # The below function will be used to access the facebook and all the stuff.


    def facebook_access (self):
        print("FACEBOOK Access for accessing and recieving facebook messages")

    # This will be used to access the instagram, so that you can access the current features

    def instagram_access (self):
        print("Granting the instagram Access and checking")

    # This function will be used to access the social medias and choose the correct social media for the particular stuff.

    # keep in mind that it can also be used for the other queries like loggin into the particular websites.
    def social_media_access (self, browse_key=""):
        print("SOCIAL MEDIA DETECTED")  # This will be used for the debugging purposes
        if browse_key != "":
            if browse_key == 'facebook':
                print("Browsing Facebook")
                webbrowser.open("www.facebook.com")
            elif browse_key == 'twitter':
                print("Browsing twitter")
                webbrowser.open("www.twitter.com")
            elif 'linkedin' == browse_key:
                print("Browsing linkedin")
                webbrowser.open("www.linkedin.com")
            elif browse_key == 'instagram':
                print("Browsing Instagram")
                webbrowser.open("www.instagram.com")
            elif browse_key == 'reddit':
                print("Browsing Reddit")
                webbrowser.open("www.reddit.com")

# Using the Image Processing !!
class Image_processing:
    def __init__(self):
        print("This is the Image processing Class , since it will be using the iopen cv 2 application")

    def Recognize_face(self):
        print("Recognition The face here!")


class Natural_processing:
    def __init__(self):
        print("NONCE!!!!")

    def recognize_text(self):
        print("")

# The Below function will be used to search on the browser and then show the desire result
def search_browser (text_input):
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


def search_wikipedia (text_input):
    # suggested_string = wikipedia.suggest(text_input)  # now going for the suggestion
    try:
        wiki_page = wikipedia.page(text_input)  # this opens up the wiki page for the particular thing
        # text_to_speech(str(wiki_page.title))  # asking the machine to speak this specified word
        # summary_text = wikipedia.summary(text_input, sentences=4)  # search on the wikipedia!
        wiki_link = str(wiki_page.url)  # Converts the url of the wiki links to the url.
        wiki_images = wiki_page.images  # Gets all the images link references. as a list
        wiki_sumry = wikipedia.summary(text_input, sentences=3)
        print(wiki_sumry)
        # webbrowser.open(wiki_link)  # opens the link on the web browser and then search the specified text link
        text_to_speech(wiki_sumry)
        return
    except:
        text_to_speech(
            "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem")
        return


# The below function is responsible for the running of the chat with the below function
# This will be used to show the Frontend for the application.

# There are two dynamic ways for storing the Frontend , since this is a Hit and run trail using the function!
# The Human computer interaction will be updated according to the software development module!
def frontend_HCI (label_text):
    root = Tk()  # This created the tkinter , face.!
    root.title("PYSHA 1.0")  # Making the Title for the Py Sha 1.0 ,
    root.geometry("300x300")  # specifying the x and the y axis in the scenario
    label1 = Label(root, text=label_text, font='size,25')  # This is the label insertion for the Tkinter module
    print(label1)  # Showing in the console for the debuggin purposes
    label1.pack()  # Packing up the label1 module in the GUI
    root.after(10000, lambda: root.destroy())  # Destroying after 10 seconds
    root.mainloop()  # Executing the main loop for the Gui Till it gets exited



def chat (input):
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

# When there is a question regerding to the self , Like the questions given to the Pysha, or the personal question about her !
# Since , The below Function is an already stored function by the developer, there are some processed required like
# Machine learning should be implemented in here too, for the particular specific questions
def Personal_PYSHA (text_input=""):
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


# this is the particular day check , that the user will be defining the day check ,since the day
#  Follows the same day check priciple for the  particular day check<!


def day_check ():
    current_date = datetime.datetime.now()
    text_to_speech("The current date is " + str(current_date.date()))
    return


# Checking the time for the computer while the

# IF the user asked for the particular time check , after the text processing this function is called ! ,
# This later calls the text to speech function using the Pyttsx for the user to speakak the particular output !
def time_check ():
    current_time = time.strftime('%H:%M:%S')
    text_to_speech("The time is " + current_time)
    return


# storing the respectable input for the user  while the computer will be able to use the resources and speak


def store_userinput (input_check):
    file_out = open("USERINPUT.txt", "a")
    file_out.writelines("USER SAID: \t" + input_check)
    file_out.write("\n")  # ending the line with the next line
    file_out.close()
    return
    # This function will be responsible for storing the responses so that it may able to answer in the future.pute


# Converting the spoken string to the speech , so that the call is Visible


def speech_to_Text ():
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

# The duration ins specified by the user, since the default value passed from the main funtion is 7 seconds,
# since the short term memory duration is 5 +- 2 So , for the maximum iof seven seconds.!!!

def record_something (duration):
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

# Machine Speaking!
def text_to_speech (text_input='HI! my name is PYSHA and i am your assistant'):
    engine = pyttsx.init()
    engine.say(text_input)
    engine.runAndWait()
    return


# Checking the input of the speech to text so that the result can cbe picked up and then stored in the displat ..!!!

# This function is responsible for the defining of the particular session and then recording the particular input, and working on the contineous
# Recognition of the voice.!

def speech_to_text_wav (file_to_recognize):
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

# The below function is responsible for the text prcessing of the Total syaing ,, since what the user i ssaying is recorded in this
def process_text_input (total_saying=""):
    total_saying = total_saying.strip()  # Stripping the string for the extra white spaces
    total_saying = total_saying.lower()  # Converting a string to lower case
    if total_saying == "quit" or total_saying.lower() == "stop listening" or total_saying.lower() == "stop" or total_saying.lower() == "exit":
        text_to_speech("I had a Great Chat with you , Bye ! My friend!")
        os._exit(0)  # exiting the program
    else:
        # this stores the Specified Input we said Regerding to something
        # Textual_Analysis(total_saying)
        '''
            Below is the place where are your working on!!!

            '''
        if total_saying.startswith('search for'):
            text_to_speech("Opening a Browser For you.")
            store_userinput("Searching on Browser :" + total_saying[10:])
            search_browser(
                text_input=total_saying[10:])  # sending every remanining thing to the Browser to browse for

        elif total_saying.startswith('social media'):
            store_userinput(total_saying)  # this stores the particular input.
            browse_key = total_saying.replace('social media',
                                              '')  # Replacing the total saying variable value'd (social media with empty string)
            browse_key = browse_key.strip()
            sma = SocialMedia()  # Creating the social media object
            sma.social_media_access(
                browse_key=browse_key)  # Passing the browser key to the social media access function.

        elif total_saying.__contains__('on wikipedia') and total_saying.startswith('search'):
            total_saying = total_saying  # this converts the string to the lower case
            total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
            total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
            text_to_speech("Searching on WIkipedia..")
            search_wikipedia(total_saying)  # calling the wikipedia search function , for the results

        elif total_saying.startswith("what is the date") or total_saying == 'date':
            # Here you will be required to input the date
            day_check()  # This calls the day check

        elif total_saying.startswith("what is the time") or total_saying == 'time':
            time_check()  # this checks the current time according to the specified state

        # Create a Grammer , that represents the questions regerding to the respectable machine

        elif total_saying.startswith("what is your"):
            # here you need to create the question saying file so that the file is readable.
            '''
                Write the Respectable question in this format so that, the Agent learns from the file.

                '''
            total_saying = total_saying.replace("what is your",
                                                "")  # replacing the words so that it will be easier for the program to Check the last thing
            Personal_PYSHA(total_saying)

        elif total_saying.startswith("text mode"):
            tm = TextMode()  # this calls the text mode function, and there we can do the processing in the form of the text!
            tm.text_mode(total_saying)  # Passes the total saying to the Class Function!
        elif total_saying == "show me a comic":
            joke_object = Joke()
            joke_object.Image_Joke()  # Calls the Joke class Image Joke Object to show a Joke in the form of an image

        elif total_saying == "tell me a joke" or total_saying == "tell me another joke":
            print("JOKE JOKE JOKE!!!")
            joke_object = Joke()
            joke_text = joke_object.joke_category()  # Calls any nerdy or Explicit joke about Chuck Norris.!
            # frontend_HCI(Joke_Text)  # calling the tkinter library to create the joke for the particular thing ,
            print(
                joke_text)  # This is the Joke text , which will be printed in the console ,since we don't have much time , working for the Console.!
            text_to_speech(joke_text)  # Speaking up the joke (By machine ) PYSHA <3

        else:
            chat(total_saying)
            # .###.....


def main ():
    print("--")
    # duration = float(input("How much time you need to record for ?"))
    # record_something(duration)  just trying to pause the thing
    client_id = ""  # this is the google api client id
    client_secret = ""  # this is the google api client secret key
    text_to_speech()  # Calls the virtual assistant to speech
    # speech_to_Text()  # calling the function
    while True:
        # try:
        record_something(7)  # providing the Duration in the Record function!
        speech_to_text_wav("output.wav")  # Converting the recorded format of WAV to speech!
        # except:
        #   text_to_speech("There is a problem with the internet connection , kindly try to configure it.!")


if __name__ == '__main__':
    main()  # Calling the main Function .!!
# The above the Audio has been recorded , and now the Audio needs to be converted into texts/
