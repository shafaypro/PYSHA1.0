import wikipedia
import webbrowser
from Text_to_speech import speak


def search_wikipedia(text_input):
    suggested_text = text_input.strip()  # strips the extra white space
    print(suggested_text)
    # suggested_string = wikipedia.suggest(suggested_text)  # now going for the suggestion
    try:
        wiki_page = wikipedia.page(suggested_text)  # this opens up the wiki page for the particular thing
        speak(str(wiki_page.title))  # asking the machine to speak this specified word
        # summary_text = wikipedia.summary(suggested_text, sentences=4)  # search on the wikipedia!
        wiki_link = str(wiki_page.url)  # Converts the url of the wiki links to the url.
        wiki_images = wiki_page.images  # Gets all the images link references. as a list
        webbrowser.open(wiki_link)  # opens the link on the web browser and then search the specified text link
        speak(wikipedia.summary(suggested_text, sentences=3))
        return
    except:
        speak(
            "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem")
        return