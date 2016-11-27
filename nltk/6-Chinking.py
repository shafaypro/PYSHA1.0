import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

'''
Chinking is basically alot of chunking, since the process of Chunking of another chunk is termed as Chinking!
Removing of a Chunk from a Chunk.
You just need to denote }{ this after the Chunking sequence , so that these are explicit out from the Data!

'''
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")  # Adding the Raw text using the state_unio from the Text file
sample_text = state_union.raw("2006-GWBush.txt")  # Adding the Sample Text With the same process using the state union

custom_sent_tokenizer = PunktSentenceTokenizer(
    train_text)  # using the Custom sentence Tokenizer which uses the Punksentence tokenizer for the training of the text

tokenized = custom_sent_tokenizer.tokenize(
    sample_text)  # Using the Custom text Tokenizer for the Tokenizing of the sample Text


def process_content ():
    try:
        for i in tokenized[0:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)   # using the regular expression to Regexly parse the Chuncked Parser
            chunked = chunkParser.parse(tagged) # Using the Parser and adding the Parsing to the Tags which have been formulated

            chunked.draw()  # Drawing the natural language Processed in the Chuncked to draw the tags!

    except Exception as e:
        print(str(e))


process_content()
