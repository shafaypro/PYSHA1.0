import nltk
import random
from nltk.corpus import movie_reviews

'''
Quick function that will find these top 3,000 words in our positive and negative documents,
marking their presence as either positive or negative:
'''


def find_features (document):
    words = set(document)  # Since we want the document to be in the form of the iteration , so we use the set
    features = {}  # Since the feature is a part of the dictionary
    for w in word_features:  # looping through the each of the words in the word features
        features[w] = (
        w in words)  # add in the boolean value, if the DOcument word is in the word , else wise add the false , A

    return features  # All the features are added and returned !


# Below is the Short Dynamic Loop function , while has the Tuple form of the

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)  # Random Shuffle Since each time the data Should be new or Unknown Repitition!

all_words = []  # Containing all the list of the words for the MovieS!

for w in movie_reviews.words():  # For each words in the Movie Reviews
    all_words.append(w.lower())  # Append all the words in the Movies Reviews ! ,

all_words = nltk.FreqDist(
    all_words)  # Frequency distribution of all the selected Words , using the natural language processing
# Keep in mind that all_words is a type of list with 2 , sub division, words and the frequency distribution like a dictionary!
#print(all_words)
word_features = list(all_words.keys())[:3000]  # List of the words of the Top #00
# print(word_features)

'''
You can pass any of the documents to the find feature function :)
'''
print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

''' for all of our documents, saving the feature existence booleans and their respective positive or negative categories by doing:'''
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# in the above sets , we have taken all the loop in the documetns since hte documents are in the form of tupple , and then Added that in the Features and a Category ,
# Since the Feature set will be in the form of a dictionary, Value , so this will be [{:} , '']
