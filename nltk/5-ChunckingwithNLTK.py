'''
Now that we know the parts of speech, we can do what is called chunking, and group words into hopefully meaningful chunks.
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