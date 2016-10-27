import webbrowser
from Text_to_speech import speak

def search_browser(text_input):
    try:
        url = 'http://google.com/search?q=' + text_input  # Creating or generating a google link for the particular file
        speak(url)
        webbrowser.open(url)
        return

    except :
        speak("I'm sorry, I couldn't reach google")  # Calling the Function so that it can be identified that ,machine can speaks for itself
        return

if __name__ == '__main__':
    search_browser("DonaldTRUMP")