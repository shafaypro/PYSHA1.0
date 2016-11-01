from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
#print(set(stopwords.words('english')))
'''
Those words which are meaning less , and doesn't help in the database , and used to Unoptimize ther performance,
This is known as Stopwords, And these words are loocated in a Specified list of stopwords.

'''

def main():
    example_sentences = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
    stop_words = set(stopwords.words('english'))  # Get the list of all the useless stop words

    word_tokens = word_tokenize(example_sentences)  # Tokenizing the sentence in to words

    # using the short lambda like function for the Filtered sentences
    filtered_sentence = [w for w in word_tokens if w not in stop_words]  # this is the list of the filtered sentence
    ''' Alternative code for the word tokenization
    for w in word_tokens: # loop through each of the word in the word tokens!
        if w not in stop_words:  # if the word is not i nStop words Then
            filtered_sentence.append(w)
    '''
    print("--------------------------------------------------")
    print(word_tokens)
    print(filtered_sentence)
if __name__ == '__main__':
    main()