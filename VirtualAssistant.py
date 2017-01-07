import datetime  # Importing the datetime for the timing modules since the date time is used to answer the questions
import os  # using the Operating systems for the particular os
import pyttsx  # Python text to speech and speech to text
import stat  # index constants for os.stat()
import time  # importing the time module for the operating systems
import urllib  # For the scrapping of the urllib
import urllib.request  # urllib requirests for the scrapping of the website.
import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
import webbrowser  # Using the web browser , For the browsing purposes
from random import *  # Using the random  function for the creation
from tkinter import *  # tkinter module will be used for the creation of the Gui of the python module!
import nltk  # natural language processing tool kt !
import pyaudio  # importing the header file of the pyaudio
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
import wikipedia  # using the wikipedia model
from PIL import Image, ImageTk  # this is the PIL Package for the Picture Image Learning
from bs4 import BeautifulSoup  # importing the beautiful soup for the web scraping !!!!!!
import wolframalpha  # this is the wolfram package which will be used , at the end for the parsing of the text
from nltk.stem import \
    PorterStemmer  # this is  the steamer which will be used for the Steaming of the Tokenized Words
from nltk.tokenize import word_tokenize, sent_tokenize, \
    PunktSentenceTokenizer  # importing both of the tokenization packages form the modules
from nltk.corpus import \
    state_union  # this imports the state union function which need to be taken in the corpus as the state union of the words.
import pygame  # pygame , python game module for the playing of the Audio files
from nltk.corpus import stopwords  # locating the stop words.

# this si the importing of the header files !
# Pre requirements : You need to Install Microsoft SDK fo Speech and all the available Tools
# Keep in mind that This is Under Heavy Construction and will be used in the later increments and

'''
// This build is heavily under progress by Muhammad Shafay Amjad, If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/PYSHA1.0
Info Dated: 23/12/2016  , WaterFall method is being Followed

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formatted as WAV, under the F.L.A.C encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

Search for <--- This opens up the browser for the result so that the Virtual assistant is able to read from the data!!!

Stop,stop listening,quit <---- This will results in the Quiting , exiting for the virtual assistant!!

search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)

what is the ----> Time, Date and others can tell you the the time ,date and others.
Ther are some other features also added in the header file , like haviing a random chat and working on different kind of
Loops

you can ask for the questions and the Answers regarding to the Natural language processing module .

If you want to ask for the Application running modules then
for that :
RUN or OPEN _________ the Underscore should be replaced by the application name
--> This script will also be monitroing the computer (Here it contains the data analysis and the data visualization part
This will be including the statistical analysis and well as the sentimental analysis . ! so that this may be used in the later
sequences of the version
--> ask for any operation ,, if other than all of the above , it will
--> You can ask the Mathematical operation as : 2+ 3 or integeration of 4 or General Knowledge.
--> Since It can also be asked the general knowledge questions like : who was the  6th president of Unitedstates


!!!!!!!!!!!!!!!!!!!!!!!EXAMPLE QUESTIONS !!!!!!!!!!!!!!!!!!!!!!!!
Who won the Election of 2016 in United states ?
Who wrote the book The lord of the Flies ?
What is the meaning of life ?
What is the meaning of Nostalgia?
bread <-- This will return the Other Requirements


--------------------------Example Programming SOlution -----------------------
ask --> Stack over flow search _____________
______ replace this with your querry
ask--> search youtube ____________ or youtube _________________
search youtube ___________________
______ replace this with your querry
or youtube ___________________


'''

''' Keep in mind to have all the back up things,
For the personal computer you need to have the computer access,
And all the other things given to the Assistant so that it can work in there.
'''
__author__ = "M Shafay Amjad"
__QA__ = "mshafayamjad@gmail.com"
__version__ = 1.0
__productname__ = "PYSHA"


# TODO : use the Wolframealpha pods to display the pictures and the solutions of the Specified questions too
class WolFrameAlphaClass:
    def __init__ (self):
        print("--------WFA--------")

    # Basic usage is pretty simple. Create the client with your App ID (request from Wolfram Alpha):
    def create_engine (self, search_input=''):  # this will create an engine
        client = wolframalpha.Client(
            app_id="23XUAT-H2875HHEEX")  # The app_id will be the application id which will be for the clientside.
        res = client.query(
            search_input)  # this will call the Client Function from the wolframaplha and then return the resources for the queries.
        for single_pod in res.pods:
            print(single_pod)  # you can do anything with the pod result here.
            # Pod objects have subpods (a Subpod is a specific response with the plaintext reply and some additional info):

            # for pod in res.pods:
            #   for sub in pod.subpods:
            #      #print(sub)
            #     print(type(sub.text))
            #    break
            # break
            # You may also query for simply the pods which have ‘Result’ titles or are marked as ‘primary’ using Result.results:
            # print(next(res.results).text)

    def search_engine (self, search_input=""):
        try:
            client = wolframalpha.Client(
                app_id="23XUAT-H2875HHEEX")  # this is the client App id specification for the PYSHA
            results = client.query(search_input)  # this searchs the input from the client side
            answer = next(
                results.results).text  # this gets the String Answered from the Search Engine . so that the answer spoken out by Pysha
            print(answer)
            return answer
        except:
            try:
                results = wikipedia.summary(search_input,
                                            sentences=2)  # this searches for the wikipedia summary input and then parse the input
                print(results)
                return results
            except:
                webbrowser.open(search_input)  # this will open the web browser
                return


# ToDO: You can improve the Search using the OAUTH and other apis of the stack over flow
class StackoverFlow:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "http://stackoverflow.com/search?q=" + search_text
        webbrowser.open(search_url)
        #


# TODO  : Use youtube api , instead of the static Youtube References
class YouTubeSearch:
    def __init__ (self):
        pass

    def search (self, search_text=''):
        search_text = search_text.strip()
        search_text = search_text.replace(' ', '+')  # This replaces the spaces with the + sign
        search_url = "https://www.youtube.com/results?search_query=" + search_text
        webbrowser.open(search_url)  # this opens the url on the webbrowser


class MusicPlayer:
    def __init__ (self):
        pygame.mixer.init()
        # this class will be responsible for the playing of the music and the specific things

    def play_music (self, song_name=""):
        pygame.mixer.music.load(song_name)  # this loads the Pygame music in the pygame module
        pygame.mixer.music.play()  # plays the music specified.
        pass  # here you will be adding the features for playing the music

    def stop_music (self):
        pygame.mixer.music.stop()  # Stops the Music Which is being played

    def play_music_start (self,
                          song_name):  # here the play music will be provided with the starting and the ending of the music.
        pass


# TODO : File Information needs to be implemented
class FileCheck:
    def __init__ (self):
        print("")

    def file_info (self, file_name=""):
        if file_name != "":
            file_stats = os.stat(file_name)
            # create a dictionary to hold file info
            file_info = {
                'fname': file_name,
                'fsize': file_stats[stat.ST_SIZE],
                'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME])),
                'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_ATIME])),
                'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_CTIME]))
            }
            print
            print("file name = %(fname)s" % file_info)
            print("file size = %(fsize)s bytes" % file_info)
            print("last modified = %(f_lm)s" % file_info)
            print("last accessed = %(f_la)s" % file_info)
            print("creation time = %(f_ct)s" % file_info)
            print
            if stat.S_ISDIR(file_stats[stat.ST_MODE]):
                print("This a directory")
            else:
                print("This is not a directory")
                print
                print("A closer look at the os.stat(%s) tuple:" % file_name)
                print(file_stats)
                print
                print("The above tuple has the following sequence:")
                print("""st_mode (protection bits), st_ino (inode number),
              st_dev (device), st_nlink (number of hard links),
              st_uid (user ID of owner), st_gid (group ID of owner),
              st_size (file size, bytes), st_atime (last access time, seconds since epoch),
              st_mtime (last modification time), st_ctime (time of creation, Windows)""")
        else:
            print("No File Detected , hence Exiting !")
            text_to_speech("No File Detected!")


# The reverse shell process is for personal use, where we will be using to ping the Updated Code, to your Home location
# Computer Code!
'''
This is the personal Computer Reverse shell!
'''


# TODO Reverse shell need to be created
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


# TODO : Jokes are needed to be fetched Other than Chuck Norris :D
# TODO : Requests for the COmic Produce error Sometimes due to the PIL header file supporting Other Formats.
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
        comic_number = random.randint(1, 1000)  # getting the commic number ranomly from the Random.rantint
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
        print(picture_file_name)
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
            try:
                print(location)  # this is just for the debugging purposes
                root = Tk()  # Creating a root element for the tkinter
                photo = PhotoImage(file=location)
                Label_img = Label(root, image=photo)
                Label_img.pack()  # This packs this image in the Loop
                root.mainloop()  # run the loop to show the gui image for the specified !
            except:
                print(location)  # this is just for the debugging purposes!
                root = Tk()  # this is the tkinter module!
                root.geometry('1000x1000')
                canvas = Canvas(root, width=999, height=999)
                canvas.pack()
                photo = Image.open(location)
                label_image = ImageTk.PhotoImage(photo)  # this adds up the photo image to the Label image
                imagesprite = canvas.create_image(400, 400, image=label_image)
                root.mainloop()

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
        # pass


# This function will tell the current weather for the Specified City , Other wise the default weather for the current city
# Using the Open weather Map for the getting the temprature for the current weather
# references are from open weather map , which is doing all the performance stuff.
class WeatherChecking:
    def __init__ (self):
        print("Weather Checking Class initialized !")

    def weather_check (text_input=""):
        print(
            'This function will be responsible for telling the current weather for the particular city or Longitude and latitude.')


# TODO : text mode needs to be created
# going in the form of the chat bot, since the particular chat bot will be used
class TextMode:
    def __init__ (self):
        print("text mode Class Accessed!")

    def text_mode (self, text_input=''):
        print("--runs the Text Mode --")
        # here you need tohave a user interface , and then provide a chatting history to!


# This will be used to launch the applications

'''
Monitor class will be responsible for the Monitoring for the cerrain syustem commands which will be kept updated again and again
'''


# TODO : Class will be Monitoring the Current PC.
class Monitor:
    def __init__ (self):
        print("Monitoring class instance has been created ")

    def monitorpersonal (self):
        pass
        print("This will be the responsible for the monitoring of the certain things happening in thecomputers")


# toDO need to create the reminders class
# Reminders, this function will be used to remind you about things.
class Reminders:
    def __init__ (self):  # this is the Constructor of the reminders
        print("Reminders Class Created !")

    def reminders_access (self, date=''):
        """

        :param date:
        """
        print(date)

    def reminder_write (self, data):
        data = str(data)  # converting the data into the string form.
        write_file = open("Reminder_way/reminder_store.txt", "w")  # this is the writing to the file specified !@
        write_file.write(data)  # this writes the data to the specified file
        write_file.close()  # closing the self file so there is no need for the writing of the File in th

    def check_reminder (self, check):
        data_read = open("Reminder_way/reminder_store.txt").readlines()
        for line in data_read:  # looping through each line of the File 1
            if line.contains(
                    check):  # if the file containes the check (means the Date which need to be checked then the reminder is called
                return check
            else:
                continue


# keep in mind that it can also be used for the other queries like loggin into the particular websites.
# These all moduels are under progress,
# Development module will be started building after 30 november 2016, !

# TODO : Social Media Access like facebook , Instagram and others
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
# TODO : if you want to detect the User Holding CUP OR STUFF use OpenCV2 here Under Construction
class ImageProcessing:
    def __init__ (self):
        print("This is the Image processing Class , since it will be using the iopen cv 2 application")

    def Recognize_face (self):
        print("Recognition The face here!")


# TODO : IMplementation of the AI
class NaturalProcessing:
    def __init__ (self):
        print("NONCE!!!!")

    def recognize_text (self):
        print("")

    def steam_word_port (self, text=""):
        if text != "":
            tokenized_word = word_tokenize(text)  # this is the word tokenized !
            ps = PorterStemmer()  # Creating a port stemmer , its basically a stemmer technique , which Gives you the stem representation of the specified Words !
            tokenized_stem_words = []  # representing a list !
            for word in tokenized_word:
                tokenized_stem_words.append(ps.stem(word))
            return

    def word_tokeniztion (self, text="", sent_tokenized=TRUE):
        if text != "":
            if sent_tokenized == True:
                Tokenized_sentence = sent_tokenize(text)
                return Tokenized_sentence
            else:
                Tokenized_words = word_tokenize(
                    text)  # this converts te passed stirng to the word tokenized for the scanning of the probability
                return Tokenized_words  # This returns the tokenized words !

    def stop_words_exclude (sentences=''):
        stop_words = set(stopwords.words('english'))  # English words are parssed out which are meaning less
        word_tokens = word_tokenize(sentences)
        filtered_sentences = [w for w in word_tokens if
                              w not in stop_words]  # this is the list of the filtered sentence
        ''' Alternative code for the word tokenization
        for w in word_tokens: # loop through each of the word in the word tokens!
            if w not in stop_words:  # if the word is not i nStop words Then
                filtered_sentence.append(w)]'''
        return filtered_sentences

    """
    One of the most powerful aspects of NLTK module is the parts of speech ,
    It CAN DO PARTS OF SPEECH TAGGING FOR YOU. This means labelling the words on the basis of NOUN, Adjectives, verbs etc.
    POS tag list:

    CC	coordinating conjunction
    CD	cardinal digit
    DT	determiner
    EX	existential there (like: "there is" ... think of it like "there exists")
    FW	foreign word
    IN	preposition/subordinating conjunction
    JJ	adjective	'big'
    JJR	adjective, comparative	'bigger'
    JJS	adjective, superlative	'biggest'
    LS	list marker	1)
    MD	modal	could, will
    NN	noun, singular 'desk'
    NNS	noun plural	'desks'
    NNP	proper noun, singular	'Harrison'
    NNPS	proper noun, plural	'Americans'
    PDT	predeterminer	'all the kids'
    POS	possessive ending	parent's
    PRP	personal pronoun	I, he, she
    PRP$	possessive pronoun	my, his, hers
    RB	adverb	very, silently,
    RBR	adverb, comparative	better
    RBS	adverb, superlative	best
    RP	particle	give up
    TO	to	go 'to' the store.
    UH	interjection	errrrrrrrm
    VB	verb, base form	take
    VBD	verb, past tense	took
    VBG	verb, gerund/present participle	taking
    VBN	verb, past participle	taken
    VBP	verb, sing. present, non-3d	take
    VBZ	verb, 3rd person sing. present	takes
    WDT	wh-determiner	which
    WP	wh-pronoun	who, what
    WP$	possessive wh-pronoun	whose
    WRB	wh-abverb	where, when
    """

    def process_content (tokenized=''):
        try:
            for i in tokenized[
                     :5]:  # here we are applying sentence limit so we can use this one for the processing the sentences.
                words = nltk.word_tokenize(i)  # Tokenizes all the word , using the word tokenize!
                tagged = nltk.pos_tag(words)  # Tags the specific words with the Natural language .
                print(tagged)  # Prints the words with the Tags in the form of the tupple .!


        except Exception as e:
            print(str(e))  # if there is an exception then this prints out the exception

    def partofspeechtag (self, sentences=''):  # th
        train_text = state_union.raw(
            "2005-GWBUSH.txt")  # This is the train text which will be used to tokenize the sample Test(unsupervised learning)
        sample_text = state_union.raw("2006-GWBUSH.txt")  # This is the sample text which will be tokenized later onward
        # print(type(sample_text))
        custom_sent_tokenizer = PunktSentenceTokenizer(
            train_text)  # This is the Train Text in the form of sentence being tokenized using the unsupervised learning.!
        # tokenized  = custom_sent_tokenizer.tokenize(sample_text) # Tokenizing he Custom sentence tokenize
        tokenized = custom_sent_tokenizer.tokenize(sentences)
        self.process_content(tokenized)


# This runs the Applications in the Program!

# TODO : more Accurate apps running
def run_apps (text_input=""):
    if text_input != "":
        if text_input == "calculator":
            os.system('calc.exe')  # Running the calculator in the Operating system
        elif text_input == "notepad":
            os.system('notepad.exe')  # Running the notepad using the Os module for the spoecified Atrtirbuote !
        elif text_input == "performance monitor":
            os.system('perfmon.exe')  # Launchign the Performance monitor from the exe
        elif text_input == "smart screen":
            os.system('smartscreen.exe')  # Working on the smart screen and running the Exe !
        elif text_input == "space agent":
            os.system('SpaceAgent.exe')  # Running the space agent for the
        elif text_input == "network status":
            os.system('netstat.exe')  # you are working ehre !
        elif text_input == "bluetooth setting":
            os.system('fsquirt.exe')  # you are working ehre !
        elif text_input == "defragment":
            os.system('Defrag.exe')  # you are working ehre !
        elif text_input == 'clean manager':
            os.system("cleanmgr.exe")
        elif text_input == "command prompt":
            os.system("cmd.exe")
        elif text_input == 'direct ex' or text_input == 'direct setting':
            os.system("dxdiag.exe")
        elif text_input == "control panel":
            os.system('control.exe')
        elif text_input == 'resource monitor':
            os.system('resmon.exe')  # this laucnhed the resource monitor to onitor the resourcr!!es of the comput
        elif text_input == "game panel":
            os.system('GamePanel.exe')
        elif text_input == 'graphic settings':
            os.system('Gfxv4_0.exe')  # this access the graphic cards
        elif text_input == 'dpi scaling':
            os.system('DipScaling.exe')  # this truns the dpi scalling for the partu
        elif text_input == 'disk partition':
            os.system('diskpart.exe')
        elif text_input == 'python' or text_input == "python interpreter":
            os.startfile(
                "C:\\Users\\Programmer\\AppData\\Local\\Programs\\Python\\Python35\\pythonw.exe")  # this calls the file location and then run the program of the python.
            # There you should run the pyton programming language so that the language will be specified by the face of the
        elif text_input == "pycharm" or text_input == "python best interpreter":
            os.startfile("C:\\Program Files (x86)\\JetBrains\\PyCharm 5.0.4\\bin\\pycharm.exe")
            # --- This runs the pycharm Compiler which can be used for the Html or the python programming
            # The Below function will be used to search on the browser and then show the desire result
        elif text_input == "movie player":
            print("started movie player!!!")
            os.startfile(
                "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")  # window media player execution!


# TODO : Exact Searching
def search_browser (text_input):
    print('-searching on browser-')
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

# TODO : WIkI Algorithum improvment
def search_wiki (text_input):
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

# TODO: Frontend HCI needs to be created !
def frontend_hci (label_text):
    root = Tk()  # This created the tkinter , face.!
    root.title("PYSHA 1.0")  # Making the Title for the Py Sha 1.0 ,
    root.geometry("300x300")  # specifying the x and the y axis in the scenario
    label1 = Label(root, text=label_text, font='size,25')  # This is the label insertion for the Tkinter module
    print(label1)  # Showing in the console for the debuggin purposes
    label1.pack()  # Packing up the label1 module in the GUI
    root.after(10000, lambda: root.destroy())  # Destroying after 10 seconds
    root.mainloop()  # Executing the main loop for the Gui Till it gets exited


# TODO : make the Chat intelligent , using the Natural language processing and AIML (artifical intelligence markup language)
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


# if there is any person question regarding to the Virtual Assistant go for this

# When there is a question regarding to the self , Like the questions given to the Pysha, or the personal question about her !
# Since , The below Function is an already stored function by the developer, there are some processed required like
# Machine learning should be implemented in here too, for the particular specific questions
# TODO : Do some of the Complex parsing
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

# TODO NOTHING
def day_check ():
    current_date = datetime.datetime.now()
    text_to_speech("The current date is " + str(current_date.date()))
    return


# Checking the time for the computer while the

# IF the user asked for the particular time check , after the text processing this function is called ! ,
# This later calls the text to speech function using the P.y.t.t.s.x. for the user to speak the particular output !
# TODO : Nothing
def time_check ():
    current_time = time.strftime('%H:%M:%S')
    text_to_speech("The time is " + current_time)
    return


# storing the respectable input for the user  while the computer will be able to use the resources and speak

# TODO: add sqlite3 database and store the input in the form of the data base
def store_userinput (input_check):
    file_out = open("USERINPUT.txt", "a")
    file_out.writelines("USER SAID: \t" + input_check)
    file_out.write("\n")  # ending the line with the next line
    file_out.close()
    return
    # This function will be responsible for storing the responses so that it may able to answer in the future.pute


# Converting the spoken string to the speech , so that the call is Visible

# TODO : speech to Text   (Google api, Microsoft Speech recording )
def speech_to_text ():
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
# TIps : Using the Wave , which is built by the microsoft
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

# This function is responsible for the defining of the particular session and then recording the particular input, and working on the continuous
# Recognition of the voice.!

def speech_to_text_wav (file_to_recognize):
    r = sr.Recognizer()

    with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file

    try:
        total_saying = r.recognize_google(audio)
        # if total_saying != "" or total_saying != NONE:
        #   text_to_speech("processing the audio")
        print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
        # text_to_speech("You said ")
        # here i will be working on latter analysis
        total_saying = str(total_saying).lower()  # converting the total saying to the strings
        process_text_input(total_saying)

    except LookupError:  # speech is unintelligible
        print("Could not understand audio")
        text_to_speech("I Couldn't understand the audio")
    except sr.UnknownValueError:
        print("UNKNOWN!!")


# The follwing function will be responsible for the text to be parsed regerding to the certain input.

# keep in mind to use the natural language processing ,, www.pythonprogramming.org

# The below function is responsible for the text prcessing of the Total syaing ,, since what the user i ssaying is recorded in this
def process_text_input (total_saying=""):
    total_saying = total_saying.strip()  # Stripping the string for the extra white spaces
    total_saying = total_saying.lower()  # Converting a string to lower case
    if total_saying == "quit" or total_saying.lower() == "stop listening" or total_saying.lower() == "stop" or total_saying.lower() == "exit":
        text_to_speech("BYE")
        os._exit(0)  # exiting the program
    else:
        # this stores the Specified Input we said Regerding to something
        # Textual_Analysis(total_saying)
        '''
            Below is the place where are your working on!!!

            '''
        if total_saying.startswith('search for') or total_saying.startswith('google '):
            text_to_speech("Opening a Browser For you.")
            store_userinput("Searching on Browser :" + total_saying[10:])
            total_saying = total_saying.replace('search for', '')  # Replacing the Search for with the total saying .
            total_saying = total_saying.replace('google', '')  # Replacing the Key word Googe with it
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

        elif (total_saying.__contains__('wikipedia') and total_saying.startswith('search')) or (
                    total_saying.__contains__('on wikipedia') and total_saying.startswith('search')):
            total_saying = total_saying  # this converts the string to the lower case
            total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
            total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
            text_to_speech('Searching on Wikipedia')
            search_wiki(total_saying)  # calling the wikipedia search function , for the results

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
            store_userinput("show me a comic")
            joke_object = Joke()  # creating an object of ht Joke class !
            text_to_speech("Fetching the Database")
            joke_object.Image_Joke()  # Calls the Joke class Image Joke Object to show a Joke in the form of an image

        elif total_saying == "tell me a joke" or total_saying == "tell me another joke":
            print("JOKE JOKE JOKE!!!")
            store_userinput("tell me a joke")
            joke_object = Joke()
            text_to_speech("OH wait")
            joke_text = joke_object.joke_category()  # Calls any nerdy or Explicit joke about Chuck Norris.!
            # frontend_HCI(Joke_Text)  # calling the tkinter library to create the joke for the particular thing ,
            print(
                joke_text)  # This is the Joke text , which will be printed in the console ,since we don't have much time , working for the Console.!
            text_to_speech(joke_text)  # Speaking up the joke (By machine ) PYSHA <3
        elif total_saying.startswith("open") or total_saying.startswith("run"):
            store_userinput(total_saying)  # This stores the Data in the Us
            # er input file so that the history is kept
            total_saying = total_saying.replace('open ', '')  # replacing the word open with the Total_saying!
            total_saying = total_saying.replace('run ', '')  # This is the replacement of the run with the
            run_apps(total_saying)  # This is the total saying being passed to the Running apps. !
        elif total_saying.startswith('parse sentence') or total_saying.startswith(
                'parse this') or total_saying.startswith('tokenize this'):
            store_userinput(total_saying)
            total_saying = total_saying.replace('tokenize this', '')
            total_saying = total_saying.replace('parse sentence',
                                                '')  # replacing the total saying with the parse sentence
            total_saying = total_saying.replace('parse this',
                                                '')  # replacing the total saying of the parse this with none !
            np = NaturalProcessing()  # creting the object of the classs
            # -------------You are working here -------------
            tokenized_sentences_return = np.word_tokeniztion(
                total_saying)  # this parse the Np with the tokenizing of the words
            print(tokenized_sentences_return)  # this prints the TOkenized the words
        elif total_saying.startswith("youtube") or total_saying.startswith(
                "search on youtube") or total_saying.startswith("search youtube") or total_saying.startswith(
            "youtube search"):
            total_saying = total_saying.replace("search", '')
            total_saying = total_saying.replace("search on youtube", "")
            total_saying = total_saying.replace("youtube", "")
            total_saying = total_saying.replace("search youtube", "")
            total_saying = total_saying.replace("youtube search", "")
            text_to_speech("Searching on youtube for : " + total_saying)
            store_userinput("Search on Youtube :" + total_saying)
            Y = YouTubeSearch()  # Creates in the Youtube Class
            text_to_speech('Displaying Results')
            Y.search(total_saying)  # Sends the Total Saying to the Youtube Search Function
            text_to_speech('Youtube Result Shown!')
        elif total_saying.startswith('stack over flow') or total_saying.startswith(
                'stackoverflow') or total_saying.startswith(
                'search stack over flow') or total_saying.startswith('stack search'):
            total_saying = total_saying.replace('stackoverflow', '')
            total_saying = total_saying.replace('stack over flow', '')
            total_saying = total_saying.replace('search stack over flow', '')
            total_saying = total_saying.replace('stack', '')
            total_saying = total_saying.replace('stack search', '')
            text_to_speech('Search on Stackoverflow' + total_saying)
            store_userinput('Search on Stackoverflow :' + total_saying)
            SOF = StackoverFlow()  # -- Creates the Object Stack over flow class and calls the search function
            SOF.search(total_saying)
            text_to_speech("Stack over flow Results Shown")
        elif total_saying.startswith('question'):
            total_saying = total_saying.replace('question', '')
            store_userinput('Question Asked : ' + total_saying)
            # since this is a computation engine that will be used for the computation of the question asked .!
            WFM = WolFrameAlphaClass()  # creating the wolframapla class that will be used for the cretion of the api assistant
            text_to_speech('searching database')
            WFM_backstring = WFM.search_engine(total_saying)  # this searches the WOlframAlpha for the Search Strings
            if WFM_backstring != "":  # if the input returned from the Wolframalpha turns out to be null then leave it .
                text_to_speech(WFM_backstring)  # this converts text to speech
                # .###.....


# TODO : Make it a little more intelligent
def main ():  # main program access
    print("--")
    # duration = float(input("How much time you need to record for ?"))
    # record_something(duration)  just trying to pause the thing
    client_id = ""  # this is the google api client id
    client_secret = ""  # this is the google api client secret key
    text_to_speech()  # Calls the virtual assistant to speech
    # speech_to_text()  # calling the function
    while True:
        # try:
        record_something(7)  # providing the Duration in the Record function!
        speech_to_text_wav("output.wav")  # Converting the recorded format of WAV to speech!
        # except:
        #   text_to_speech("There is a problem with the internet connection , kindly try to configure it.!")


if __name__ == '__main__':
    main()  # Calling the main Function .!!
# The above the Audio has been recorded , and now the Audio needs to be converted into texts/

#Machine Learning book + NLTK BOOK need to be studied  with Plotting and OPENCV2

## Work with the MEGA VOICE COMMAND AFTER THE EXAM HAVE BEEN FINISHED.
