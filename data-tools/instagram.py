import json
import itertools
import csv
import os
#import matplotlib.pylab as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
#from nltk.corpus import stopwords
# import sentiment function
import sys
sys.path.append("lib/") 
from sentiment import SIA
# ingest JSON data
with open('messages.json') as f:
    data = json.load(f)
# define your instagram user account or the id of AI avatar you wish to analyze
ig_user = "plant_group"   
# empty list
participants_list = []
#print(data)
messageCount = len(data)
for message in data:
    #print(message)
    participants = message['participants']
    print(participants)
    participants_list.append(participants)
    print("=======================================================")

#print(participants_list)
# now flatten participant list of lists
participant_list = list(itertools.chain(*participants_list))
# remove duplicates from list
participant_list = list(dict.fromkeys(participant_list))
print(participant_list)

#empty list for conversations
user_conversations_list = []
# message timestamp list
user_conversation_ts = []
#empty dictionary for storing timestamp and message
user_convo_dic = {}

# cycle through your conversations
for message in data: 
    conversations = message['conversation']
    for i in conversations:
        if i['sender'] == ig_user:
            #print(ig_user)
            user_conversation_ts.append(i['created_at'])
            try:
                # this gives us a dic with timestamp and the message
                user_conversations_list.append(i['text'])
                user_convo_dic[i['created_at']] = i['text']
            except:
                # no text, meaning they sent  emoji 
                pass   

#print(user_conversation_ts)
#print(user_conversations_list)
# dictionry of timestamped messages from your user -- in this case "plant_group"
#print(user_convo_dic)

# Tokenize words for NLP 
#tokens_list = []
#
#for item in user_conversations_list:
#    try:
#        tokens = [t for t in item.split()]
#        #print(tokens)
#        tokens_list.append(tokens)
#    except:
#        pass
#    
#print(tokens_list)
# now flatten token list of lists
# token_list = list(itertools.chain(*tokens_list))
#print(token_list)

#sid = SentimentIntensityAnalyzer()
#for sentence in user_conversations_list:
#    print(sentence)
#    try:
#        ss = sid.polarity_scores(sentence)
#        for k in sorted(ss):
#            print('{0}: {1}, '.format(k, ss[k]), end='')
#
#    except:
#        pass
#    

# call sentiment analyzer function on sentences 
SIA = SIA(user_conversations_list)
print(SIA)
# VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media
# positive sentiment : (compound score >= 0.05)
# neutral sentiment : (compound score > -0.05) and
# negative sentiment : (compound score <= -0.05)

