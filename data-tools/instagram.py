import json
import itertools
import csv
import os
#from nltk.corpus import stopwords
#import matplotlib.pylab as plt

with open('messages.json') as f:
    data = json.load(f)

# define your instagram user account
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
# dictionayry of timestamped messages from your user -- in this case "plant_group"
#print(user_convo_dic)

# Tokenize words for NLP 
tokens_list = []

for item in user_conversations_list:
    try:
        tokens = [t for t in item.split()]
        #print(tokens)
        tokens_list.append(tokens)
    except:
        pass
    
#print(tokens_list)
# now flatten token list of lists
token_list = list(itertools.chain(*tokens_list))
print(token_list)
