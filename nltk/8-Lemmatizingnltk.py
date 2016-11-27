import nltk
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer # Word net lemmatzier
'''
A very similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier,
stemming can often create non-existent words, whereas lemmas are actual words.
So, your root stem, meaning the word you end up with, is not something you can just look up in a dictionary, but you can look up a lemma.
Some times you will wind up with a very similar word, but sometimes, you will wind up with a completely different word. Let's see some examples.
'''
lemmatizer = WordNetLemmatizer() # Created a Lemmatizer Object
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))  # Keep in mind, this is the specification of the part of speech tag , the default value is the noun!
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))
'''
Here, we've got a bunch of examples of the lemma for the words that we use. The only major thing to note is that lemmatize takes a part of speech parameter,
 "pos." If not supplied, the default is "noun." This means that an attempt will be made to find the closest noun, which can create trouble for you. Keep this in mind
  if you use lemmatizing!
'''