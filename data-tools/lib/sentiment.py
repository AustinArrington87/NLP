import json
import itertools
import csv
import os
#from nltk.corpus import stopwords
#import matplotlib.pylab as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def SIA (user_conversations_list):
    sid = SentimentIntensityAnalyzer()
    for sentence in user_conversations_list:
        print(sentence)
        try:
            ss = sid.polarity_scores(sentence)
            for k in sorted(ss):
                print('{0}: {1}, '.format(k, ss[k]), end='')

        except:
            pass