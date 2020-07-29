from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

# VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media

sentences = ["VADER is smart, handsome and funny.", # positive sentence
    "VADER is smart, handsome, and funny!", # punctuation emphasis (intensity adjusted) 
    "VADER is very smart, handsome, and funny.", # booster word (intensity adjusted) 
    "VADER is VERY SMART, handsome, and FUNNY.", # emphasis for ALLCAPS handled
    "VADER is VERY SMART, handsome, and FUNNY!!!", #combination of signals - adjusts intensity
    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!", # booster + punctuation
    "The book was good.", # positive sentence
    "The book was kind of good", # qualified positive sentence (intensity adjusted)
    "The plot was good, but the characters are uncompelling and the dialog is not great.", #mixed
    "A really bad, horrible book.", # negative sentence with boosters
    "At least it isn't a horrible book.", # negated negative sentence w/ contraction
    " :) and :D", # emoticons
    "", # empty string
    "Today sux", # negative slang
    "Today sux!", # negative slang with punctuation emphasis
    "Today SUX!", # negative slang with Caps emphasis
    "Today kinda sux! But I'll get by, lol" # mixed sentiment w slang & constrastive conjunction
]

paragraph = "It was one of the worst movies I've seen, despite good reviews. \
    Unbelievably bad acting!! Poor direction. VERY poor production. \
    The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

lines_list = tokenize.sent_tokenize(paragraph)
# add tokens from our paragraoh to sentence list
sentences.extend(lines_list)

# let's look at some trickier sentences and add to our list 
tricky_sentences = [
    "Most automated sentiment analysis tools are shit.",
    "VADER sentiment analysis is the shit.",
    "Sentiment analysis has never been good.",
    "Sentiment analysis with VADER has never been this good.",
    "Luke Skywalker has never been so entertaining.",
    "I won't say that the movie is astounding and I wouldn't claim that \
    the movie is too banal either.",
    "I like to hate George Lucas films, but I couldn't fault this one",
    "It's one thing to watch a Michael Bay film, but another thing entirely \
    to pay for it",
    "The movie was too good",
    "This movie was actually neither that funny, nor super witty.",
    "This movie doesn't care about cleverness, wit or any other kind of \
    intelligent humor.",
    "Those who find ugly meanings in beautiful things are corrupt without \
    being charming.",
    "There are slow and repetitive parts, BUT it has just enough spice to \
    keep it interesting.",
    "The script is not fantastic, but the acting is decent and the cinematography \
    is EXCELLENT!",
    "Roger Dodger is one of the most compelling variations on this theme.",
    "Roger Dodger is one of the least compelling variations on this theme.",
    "Roger Dodger is at least compelling as a variation on the theme.",
    "they fall in love with the product",
    "but then it breaks",
    "usually around the time the 90 day warranty expires",
    "the twin towers collapsed today",
    "However, Mr. Carter solemnly argues, his client carried out the kidnapping \
    under orders and in the ''least offensive way possible.''"
]

# positive sentiment : (compound score >= 0.05)
# neutral sentiment : (compound score > -0.05) and
# negative sentiment : (compound score <= -0.05)

sentences.extend(tricky_sentences)
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')



