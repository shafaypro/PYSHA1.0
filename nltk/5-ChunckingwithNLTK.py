import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
'''ow that we know the parts of speech, we can do what is called chunking, and group words into hopefully meaningful chunks.
One of the main goals of chunking is to group into what are known as "noun phrases." These are phrases of one or more words
that contain a noun, maybe some descriptive words, maybe a verb,  and maybe something like an adverb. The idea is to group
nouns with the words that are in relation to them.
'''

"""In order to chunck we can use the regular expressiono, we are going to utilize the follwing
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
. = Any character except a new line
"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer



def process_content():
    try:
        for i in tokenized[0:1]:   # since the tokenized has a complete list of words
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)  # this is the c
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""  # Specifing the regular exprssion of
            chunkParser = nltk.RegexpParser(chunkGram)  # using a regular expression string to create a chunck parser for the particular work on the chunk.

            chunked = chunkParser.parse(tagged)  # this is the parsing of the tags which are applied to the sentences
            chunked.draw()  # drawing the natural language processed data to show what is going on !
            for subtree in chunked.subtrees(): # Since each chunked has sub tress , having chunked and non chuncked.! so we can loop through it .!
                print(subtree)  # printing the specified chunked tree for the particular chunck.!! This prints the specified chunk
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    train_text = state_union.raw("2005-GWBush.txt") # using the state union function to get the raw input from the specific file.
    sample_text = state_union.raw("2006-GWBush.txt")  # using the sample text as a state union raw input.!
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)   # Applying the unsupervised learning on the punksentence tokenizer, using the applied text
    tokenized = custom_sent_tokenizer.tokenize(sample_text) # Using the previous Learning and applying on the another sample text which we need to parse
    process_content()  # Calling the process content function for the spe