import wolframalpha  # this imports wolframalpha api
import wikipedia  # this imports the wikipedia
import webbrowser # this will be used to search the web
from xml.etree.ElementTree import ElementTree as ET
'''
This is a computational Knowledge engine , that has the ability of the natural language processing,
Which can generate text on the Basis of the wolframalpha
'''


class WolFrameAlphaClass:
    def __init__ (self):
        print("Wolframe Alpha Has been Intialiazed !")

    # Basic usage is pretty simple. Create the client with your App ID (request from Wolfram Alpha):
    def create_engine(self, search_input=''):  # this will create an engine
        client = wolframalpha.Client(
            app_id="23XUAT-H2875HHEEX")  # The app_id will be the application id which will be for the clientside.
        res = client.query(search_input)  # this will call the Client Function from the wolframaplha and then return the resources for the queries.
        for single_pod in res.pods:
            print(single_pod)  # you can do anything with the pod result here.
            # Pod objects have subpods (a Subpod is a specific response with the plaintext reply and some additional info):

        #for pod in res.pods:
         #   for sub in pod.subpods:
          #      #print(sub)
           #     print(type(sub.text))
            #    break
            #break
            # You may also query for simply the pods which have ‘Result’ titles or are marked as ‘primary’ using Result.results:
            #print(next(res.results).text)
    def search_engine(self,search_input = ""):
        try:
            client = wolframalpha.Client(app_id="23XUAT-H2875HHEEX")  # this is the client App id specification for the PYSHA
            results = client.query(search_input)  # this searchs the input from the client side
            answer = next(results.results).text  # this gets the String Answered from the Search Engine . so that the answer spoken out by Pysha
            print(answer)
        except:
            try:
                 results = wikipedia.summary(search_input,sentences=2)  # this searches for the wikipedia summary input and then parse the input
                 print(results)
            except:
                webbrowser.open(search_input)  # this will open the web browser
                pass
def main():
    WFA = WolFrameAlphaClass()
    text_search = input("Enter the query you want to search for : ")
    WFA.search_engine(text_search) # this Lets the Text to be searched and then parsed in to

main()