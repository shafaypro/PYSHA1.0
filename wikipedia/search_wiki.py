import wikipedia
import pyttsx
def search_on_wiki():
    text_items =wikipedia.search("Black Holes")
    #k = wikipedia.suggest('black holes')
    #print(k)
    #print(str(k))
    #print(text_items)
    #wikipedia.suggest("Barak Obama") # You can use this to have the corrected title for the search string.

    #page_search = wikipedia.page(str(k))
    #print(page_search.title)  # prints the title of the page
    Engine_check = pyttsx.init() # this is the intialization of the Text to speech!
    # Engine_check.say(page_search.content)
    Engine_check.say(wikipedia.summary("What", sentences=4))
    Engine_check.runAndWait()


if __name__ == '__main__':
    search_on_wiki()
