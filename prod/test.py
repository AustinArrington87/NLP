#  conda install -c conda-forge spacy
# python -m spacy download en_core_web_sm

import spacy

#Load english tokenizer, tagger, parser, NER, word vectors
nlp = spacy.load("en_core_web_sm")

# process whole docs 

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

doc = nlp(text)

# analyze syntax 
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos == "VERB"])

# find named entities, concepts, phrase s
for entity in doc.ents:
    print(entity.text, entity.label_)

#########################################  
    
# import english lang class 
from spacy.lang.en import English
nlp = English()

doc = nlp("Hello world!")
for token in doc:
    print(token.text)

print(doc[0])

span = doc[1:3]
print(span)

######## Token attributes 
doc = nlp("It costs $5")

print("Index: ", [token.i for token in doc])
print("Text: ", [token.text for token in doc])
print("is_alpha: ", [token.is_alpha for token in doc])
print("is_punct: ", [token.is_punct for token in doc])
print("like_num: ", [token.like_num for token in doc])











    
    
    
    