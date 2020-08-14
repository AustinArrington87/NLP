import spacy
from spacy.lang.en import English

nlp = English()

# Import the Doc and Span classes
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])


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
            print("Found proper noun before verb", token.text)

