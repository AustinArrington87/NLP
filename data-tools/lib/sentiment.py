from nltk.sentiment.vader import SentimentIntensityAnalyzer

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