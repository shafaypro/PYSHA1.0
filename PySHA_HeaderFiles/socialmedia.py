import webbrowser
import random
import selenium
from selenium import webdriver  # Package for the browsing andthe accessing of the web drivers.!
import time


class SocialMedia:
    def __int__ (self):
        print("This is the Constructor of the class Social media")

    # The below function will be used regerding to the twitter accessing and stuff
    def twitter_access (self):
        c_browser = webdriver.Chrome()  # Create a webdriver of chrome , this can be replaced by the firefox or the opera
        c_browser.get('https://twitter.com')  # Fetching the url of the twitter
        # time.sleep(10)  # putting the ocmputer to the sleep !
        # user_email = c_browser.find_element_by_id('signin-email')  # finding the
        # user_email.send_keys("shafay1990@hotmail.com") # this sends or replace the value for the signint_email
        # user_pw = c_browser.find_element_by_id('signin-password')  # Finding the password element so that it can be accessed.
        # user_pw.send_keys("########")  # Fetching the keys for the particular world
        # login = c_browser.find_element_by_class_name('submit btn primary-btn flex-table-btn js-submit')  # Login button is found by this class
        # login.click() # Click event is generated using this module .!
        # print("Granting the twitter Access")
        c_browser.quit()

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


def main ():
    sma = SocialMedia()
    sma.twitter_access()  # Twitter Function Called


if __name__ == '__main__':
    main()  # Calls the main function !
