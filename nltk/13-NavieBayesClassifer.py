import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize  # using the word and the sentence tokenizer
from nltk.corpus import movie_reviews  # the source of the data set is in here
import random  # This will be used to shuffe the dataset

'''
1) Spreading the data in to training and the testing sets
What is Native bayes Classifer ?
 In machine learning, naive Bayes classifiers are a family
 of simple probabilistic classifiers based on applying Bayes'
 theorem with strong (naive) independence assumptions between
 the features.
    P(Ck| L ) = P(Ck) p(x|Ck)/ P(x)
Before we can train and test our algorithm, however, we need to go
ahead and split up the data into a training set and a testing set.

TIPS:
You could train and test on the same dataset, but this would present you with some serious bias issues,
so you should never train and test against the exact same data.

we'll assign the first 1,900 shuffled reviews, consisting of both positive and negative reviews, as the training set.
 Then, we can test against the last 100 to see how accurate we are.

This is called supervised machine learning, because we're showing the machine data, and telling it "hey, this data is
positive," or "this data is negative." Then, after that training is done, we show the machine some new data and ask the
 computer, based on what we taught the computer before, what the computer thinks the category of the new data is.




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

# ---- training the sets ------

# Set which we are hoing to train it
training_set = featuresets[:1900]  # This is the 5-15 percent of the data set

# Set which we will test against
testing_sets = featuresets[1900:]  # This is the 80-85% of the data set

# Defining the Classifier which will have the set which have been trained >!

# So for that
classifier = nltk.NaiveBayesClassifier.train(
    training_set)  # This calls the bayes law and then traine the text for the machine learning purpposes !
# Package.Class.Function(data)

# NOw the data is trained !
print("Native Bayes law Accuracy percentage", (nltk.classify.accuracy(classifier, testing_sets)) * 100)
classifier.show_most_informative_features(15)  # this calls the classified and show the most informative session !
# since the classifier for the most informative session returns the particular value for the Specified Integet values .


# -- We need to have realibility and the Reasonability Accuracy
# Both of these can be improved on the Basis of the Algorithum