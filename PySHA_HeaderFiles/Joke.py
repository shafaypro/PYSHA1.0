import random
import os
import image
import requests
from bs4 import BeautifulSoup  # importing the beautiful soup for the web scraping !!!!!!
import urllib.request  # urllib requirests for the scrapping of the website.
from tkinter import *
import json
import requests


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
        print("This will tell the joke about something")

    def joke_category (self, category=["nerdy,explicit"]):
        # print("this is the Joke Category list which will scrap the site and provide the Joke regerding to the Category")
        print(str(category))
        joke_web_api_link = "http://api.icndb.com/jokes/random?limitTo=[" + str(
            category) + "]"  # Limiting the link with the specification for the particular category !
        scrapped_page = str(urllib.request.urlopen(
            joke_web_api_link).read())  # Reading all the requested Scrapped Page from the Api , to see the page .
        # print(scrapped_page[:])
        # Its need a fixing script here that would parse the json unformed file .!
        print(scrapped_page)
        joke_start = scrapped_page.find('"joke": ') + 9
        joke_end = scrapped_page[joke_start:].find('"categories"')
        joke_text = scrapped_page[joke_start:joke_start + joke_end]
        self.show_image('',joke_text)


if __name__ == '__main__':
    J = Joke()
    # J.random_joke()
    # J.Image_Commic()  # this calls the Comic function .!
    J.joke_category()
