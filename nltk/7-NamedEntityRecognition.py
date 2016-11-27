import nltk
from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

'''
One of the most major forms of chunking in natural language processing is called "Named Entity Recognition."
The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations, monetary figures, and more.
This can be a bit of a challenge, but NLTK is this built in for us. There are two major options with NLTK's named entity
recognition: either recognize all named entities, or recognize named entities as their respective type, like people, places, locations, etc.
'''


def process_content ():
    try:
        for i in tokenized[6:7]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)  # Adds the post tags to the Parsed text
            named_Ent = nltk.ne_chunk(tagged, binary=True) # The binary is used for showing the Tags BAse and the Pulling the entities out
            # If you set the Binary to false then
            named_Ent= nltk.ne_chunk(tagged,binary=False)
            named_Ent.draw() # Draws with the Tagging of the Named Entity , which the machine knows the name of those !
    except Exception as e:
        print(str(e))


train_text = state_union.raw('2005-GWBush.txt')  # This is the trained text on which the machine will be trained !
sample_text = state_union.raw('2006-GWBush.txt')  # picking the Text which will be used to be tokenized
custom_sent_tokenize = PunktSentenceTokenizer(
    train_text)  # using the punkbuster tokenizer for the tokenizing of the Intial text
tokenized = custom_sent_tokenize.tokenize(sample_text)  # tokenizing the sample text
process_content()

'''Immediately, you can see a few things. When Binary is False, it picked up the same things, but wound up
splitting up terms like White House into "White" and "House" as if they were different, whereas we could see in the binary =
 True option, the named entity recognition was correct to say White House was part of the same named entity.

Depending on your goals, you may use the binary option how you see fit. Here are the types of Named Entities that you can get if you have binary as false:

NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''