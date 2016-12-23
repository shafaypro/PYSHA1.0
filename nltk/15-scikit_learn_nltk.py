import random
import nltk
from nltk.corpus import movie_reviews
from sklearn.naive_bayes import Multi BNnomialNB, BernoulliNB
from nltk.classify.scikitlearn import SklearnClassifier
from numpy._distributor_init import NUMPY_MKL
def find_features(document):
    words = set(document)  # Since we want the document to be in the form of the iteration , so we use the set
    features = {}  # Since the feature is a part of the dictionary
    for w in word_features:  # looping through the each of the words in the word features
        features[w] = (
            w in words)  # add in the boolean value, if the documents word is in the word , else wise add the false , A
    return features  # All the features are added and returned !
# Below is the Short Dynamic Loop function, while has the Tuple form of the
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)  # Random Shuffle Since each time the data Should be new or Unknown Repitition!
all_words = []  # Containing all the list of the words for the MovieS!
for w in movie_reviews.words():  # For each words in the Movie Reviews
    all_words.append(w.lower())  # Append all the words in the Movies Reviews ! ,
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]  # List of the words of the Top #00
print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
''' for all of our documents, saving the feature existence booleans and their respective positive or negative categories by doing:'''
featuresets = [(find_features(rev), category) for (rev, category) in documents]
training_set = featuresets[:1900]  # This is the 5-15 percent of the data set
testing_sets = featuresets[1900:]  # This is the 80-85% of the data set
##classifier = nltk.NaiveBayesClassifier.train(training_set)
#print("Native Bayes law Accuracy percentage", (nltk.classify.accuracy(classifier, testing_sets)) * 100)
#classifier.show_most_informative_features(15)


# There are two different variations for the Bayes theorm , using the Scikit learn module , You can have the Ability for the Specification for the Miltinomial and Bernouli Modules.
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:", nltk.classify.accuracy(MNB_classifier, testing_sets))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:", nltk.classify.accuracy(BNB_classifier, testing_sets))