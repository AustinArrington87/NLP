#import spacy
#
#from spacy.matcher import Matcher
#
## load model, create nlp object
#nlp = spacy.load("en_core_web_sm")
## initialize matcher
#matcher = Matcher(nlp.vocab)
## add pattern to matcher
#pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
#matcher.add("IPHONE_PATTERN", None, pattern)
#
## process  text 
#doc = nlp("Upcoming iPhone X release date leaked.")
#
## find named entities, concepts, phrase s
#matches = matcher(doc)
#
#for match_id, start, end in matches:
#    # matched span
#    matched_span = doc[start:end]
#    print(matched_span.text)

import spacy

# Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"},{"TEXT": "X"}]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", None, pattern)

# Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])