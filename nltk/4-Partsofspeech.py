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

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer  # The Tokenizer which will be used.

'''This tokenizer is capable of unsupervised machine learning --> PuckSentenceTokenizer '''
'''o you can actually train it on any body of text that you use. First, let's get some imports out of the way that we're going to use:'''
def process_content():
    try:
        for i in tokenized[:5]:  # here we are applying sentence limit so we can use this one for the processing the sentences.
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)  # Tags the specific words with the Natural language .
            print(tagged)

    except Exception as e:
        print(str(e))



if __name__ == '__main__':
    train_text = state_union.raw("2005-GWBUSH.txt")   # This is the train text which will be used to tokenize the sample Test(unsupervised learning)
    sample_text = state_union.raw("2006-GWBUSH.txt")  # This is the sample text which will be tokenized later onward
    custom_sent_tokenizer = PunktSentenceTokenizer(
        train_text)  # This is the Train Text in the form of sentence being tokenized using the unsupervised learning.!
    tokenized  = custom_sent_tokenizer.tokenize(sample_text) # Tokenizing he Custom sentence tokenize
    process_content()