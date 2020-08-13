import spacy

#Load english tokenizer, tagger, parser, NER, word vectors
nlp = spacy.load("en_core_web_sm")

doc = nlp("I love coffee")
# each word has a database entry 
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])

#  lexeme = context-indepeendent info about a word 
lexeme = nlp.vocab["coffee"]
# print "lexical" aka vocab attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)

####

from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

########3
doc = nlp("David Bowie is a PERSON")

# Look up the hash for the string label "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Look up the person_hash to get the string
person_string = nlp.vocab.strings[person_hash]
print(person_string)

##########

