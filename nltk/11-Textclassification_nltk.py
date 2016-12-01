import nltk
from nltk.corpus import movie_reviews  # This imports the specified File for the reviews of the movies
import random

"""
Text classification : Trying to Classify the text  is termed as text Classification . Since it can be in different ways.
Maybe we're trying to classify text as about politics or the military. Maybe we're trying to classify it
by the gender of the author who wrote it. A fairly popular text classification task is to identify a body
of text as either spam or not spam, for things like email filters. In our case, we're going to try to create a sentiment analysis algorithm.

This methodologies can be applied in each and every category , since there are only two ways
Spam or not spam , So the sentimental analysis is like POistive , Highly positive, negative , Low negative
"""
# You can use anything you want !
'''
There are two ways to get the Movie review words and the Categories of the words as given in the Sceniro
documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)
            ]
'''

# this is for creating and testing the sets !!!
documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

# When you are training the text you need to have the different data , because all the data should be new whenever runs.
random.shuffle(documents)  # This shuffles the set Tuple of the Documents !
# print(documents[1])
# First take all the words which are the most popular words , then you search for the negative and the  00positive words
# If the words are Positive or negative on the basis of that you need to check the list

all_words = list()
for w in movie_reviews.words():
    all_words.append(str(
        w).lower())  # adding the All words to the List of the Words , since these are the words which are taken out from the movie reviews.!
''
all_words = nltk.FreqDist(all_words)  # adding the Frequeny for the Words as
# print(all_words.most_common(12)) # To show the to 12 most common used words!  there are different kind of the words so keep in mind using the frequencies
print(all_words["stupid"])  # this shows the occurence of the word stupid , since the answer should be 253
