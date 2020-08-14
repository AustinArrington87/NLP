import spacy
from spacy.lang.en import English

nlp = English()

from spacy.tokens import Doc

#spaCy is cool!"

words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# create doc from words and spaces 
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Desired text: "Go, get started!"
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]
# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)



##############################################
nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin looks like a nice city")

# find proper noun followed by verb 
# iterate over tokens 
for token in doc:
    # is current token proper noun
    if token.pos_ == "PROPN":
        # next token verb
        if doc[token.i +1].pos_ == "VERB":
            print("Found proper noun before verb:", token.text)
            
            

