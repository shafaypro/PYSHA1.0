from nltk.tokenize import sent_tokenize, \
    word_tokenize  # importing both of the sentence tokenization and word tokenization
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer  # This is the porter stemmer which is been used since 1979

'''
The process of steaming is having the base root of something and trying to shorted the length of the text
without changing the meaning of it. Sort of a normalization method.
Why we steam ?
To shorten the lookup and normalize sentences.
Consider the following example /
I was taking a ride in the car.
I was riding in the car.
This sentence means the same thing. in the car is the same. I was is the same. the ing denotes a clear past-tense in both cases, so is it truly necessary to differentiate
between ride and riding, in the case of just trying to figure out the meaning of what this past-tense activity was?
No, not really.This is just one minor example, but imagine every word in the English language, every possible tense and affix you can put on a word. Having individual
dictionary entries per version would be highly redundant and inefficient, especially since, once we convert to numbers, the "value" is going to be identical.

One of the most popular stemming algorithms is the Porter stemmer, which has been around since 1979.

'''
def stem_sentence(sentence):
    ps = PorterStemmer()  # Creating the port stemmer.!
    words = word_tokenize(sentence)
    print("-------------------------------------------------------")
    for w in words:
        print(ps.stem(w))

def main():
    print("")
    ps = PorterStemmer()  # defining the port stemmer
    example_words = ["python", "pythoner", "pythoning", "pythoned",
                     "pythonly"]  # These are the particular words you want to be stammed

    # The below is used to generate the steaming of the example words. !!!
    for w in example_words:
        print(ps.stem(w))  # Prints the word which is stemmed , after.!

    # Passing a sentence and then breaking it down in to words and then printing the steam words from it .!!!
    new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
    stem_sentence(new_text) # Calling the function stem sentence to pass it to the Stemmer and then print all the steams of the words.

if __name__ == '__main__':
    main()  # calling the main function!
