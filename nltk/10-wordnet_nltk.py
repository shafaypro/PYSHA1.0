import nltk
from nltk.corpus import wordnet  # This takes few Seconds

'''One of the more advanced data sets in here is "wordnet."
 Wordnet is a collection of words, definitions, examples of their use, synonyms,
 antonyms, and more. We'll dive into using wordnet next.'''

'''
WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus.
You can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more. Let's cover some examples
'''
syns = wordnet.synsets("program")
print(syns[0])  # you can refer to the particular word ,
# You can also use the lemmas
print(syns[0].name())  # Prints out the names for the Synonyms of the words net , which is passed to the Data!
print(syns[0].lemmas()[
          0].name())  # This First Lematize the Sysns and then parse that to the name , to get the only name for the aLemmas
# To check the Definition for hte syns.
print(syns[0].definition())
# To check the Examples , for the particular sentence is like
print(syns[0].examples())

'''
Next, how might we discern synonyms and antonyms to a word?
The lemmas will be synonyms, and then you can use .antonyms to
find the antonyms to the lemmas. As such, we can populate some lists like:
'''

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):  # take the Word Good, and look up for the synsets
    for l in syn.lemmas():  # if all the Pump down lemmas , loop through it
        synonyms.append(l.name())  # Add all the Synonyms to that
        if l.antonyms():  # If the particular lemma has Antonym
            antonyms.append(l.antonyms()[0].name())  # add the first Antonym name in it

print(set(synonyms))
print(set(antonyms))
# Comparing the two words
w1 = wordnet.synset('ship.n.01')  # This picks up the words  which need to be compared!
w2 = wordnet.synset('boat.n.01')  # This compares the word2 which is to be compared !
print(w1.wup_similarity(w2))  # Checking the Similarity between the words!

# ----------------------------------------------- #

w1 = wordnet.synset('ship.n.01')

w2 = wordnet.synset('car.n.01')

print(w1.wup_similarity(w2))

# ----------------------------------------------- #

w1 = wordnet.synset('ship.n.01')

w2 = wordnet.synset('cat.n.01')

print(w1.wup_similarity(w2))

# -----------------------------------------------#
