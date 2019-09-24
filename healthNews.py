import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import matplotlib.pylab as plt

# DESCRIPTION 
# Webscrape and frequency analyze the lastest Health News 
# Install nltk: $ pip install --user -U nltk
# To load modules open Python shell and enter >>> import nltk >>> nltk.download()

response = urllib.request.urlopen('https://www.healthline.com/health-news')
html = response.read()
#print(html)
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip = True)
#print(text)
# tokenize words 
tokens  =  [t for t in text.split()]
#print(tokens)

# remove stop words (am, at, the, for) and count frequency
sr = stopwords.words('english')
chars = ["{", "=", "-", "}", "+", "_", "--", ">", "<", "<=", ">=", "—", "var"]
conjunctions = ["but", "But", "and", "or", "nor", "because", "although", "since", "unless", "while", "where"]
conjugations =  ["Is", "is", "Am", "am", "Are", "are", "Was", "was", "Were", "were", "Being", "being", "Been", "been"]
clean_tokens = tokens[:]
for token in tokens:
	if token in sr:
		clean_tokens.remove(token)
# calculate frequency
freq = nltk.FreqDist(clean_tokens)
wordFreqDic = {}
freqDic5 = {}
freqDic10 = {}
freqDic25 = {}
freqDic50 = {}
freqDic100 = {}

# function to remove special characters and conjunnctions
def removeWord(wordList, wordDic):
	for word in wordList:
		if word in wordDic:
			del wordDic[word]

# bucket dictionaries by increasing word frequency 
for key,val in freq.items():
	if val >= 5:
		#print(key)
		freqDic5.update({key: val})
		removeWord(chars, freqDic5)
		removeWord(conjunctions, freqDic5)
		removeWord(conjugations, freqDic5)
	elif val >= 10:
		#print(key)
		freqDic10.update({key: val})
		for char in chars:
			if char in chars:
				del freqDic10[char]
	elif val >= 25:
		#print(key)
		freqDic25.update({key: val})
		for char in chars:
			if char in chars:
				del freqDic25[char]
	elif val >= 50:	
		#print(key)
		freqDic50.update({key: val})
		for char in chars:
			if char in chars:
				del freqDic50[char]
	elif val >= 100:
		#print(key)
		freqDic100.update({key: val})
		for char in chars:
			if char in chars:
				del freq100[char]
	else:
		pass
	wordFreqDic.update({key: val})
	#print(str(key) + ":" + str(val))

totalDicLen = len(wordFreqDic)
print("Word Occurrences: " + str(totalDicLen))
# bucket out words by increasing  number of occurrences
freqDic5Len = len(freqDic5)
if freqDic5Len > 0:
	over5 = freqDic5Len/totalDicLen
	print("###############")
	print(">= 5 Word Occurrences:")
	print(str(freqDic5Len)+ " words occuring 5 or more times, or " + str(round((100*over5),2)) + "% of the total")
	print(" ")
	print(freqDic5)
	print("---------------------")	
freqDic10Len = len(freqDic10)
if freqDic10Len > 0:
	over10 = freqDic10Len/totalDicLen
	print("###############")
	print(">= 10 Word Occurrences:")
	print(str(freqDic10Len)+ " words occuring 10 or more times, or " + str(round((100*over10),2)) + "% of the total")
	print(" ")
	print(freqDic10)
	print("---------------------")
freqDic25Len = len(freqDic25)
if freqDic25Len > 0:
	over25 = freqDic25Len/totalDicLen
	print("###############")
	print(">= 25 Word Occurrences:")
	print(str(freqDic25Len)+ " words occuring 5 or more times, or " + str(round((100*over25),2)) + "% of the total")
	print(" ")
	print(freqDic5)
	print("---------------------")
freqDic50Len = len(freqDic50)
if freqDic50Len > 0:
	over50 = freqDic50Len/totalDicLen
	print("###############")
	print(">= 50 Word Occurrences:")
	print(str(freqDic50Len)+ " words occuring 5 or more times, or " + str(round((100*over50),2)) + "% of the total")
	print(" ")
	print(freqDic50)
	print("---------------------")
freqDic100Len = len(freqDic100)
if freqDic100Len > 0:
	over100 = freqDic100Len/totalDicLen
	print("###############")
	print(">= 100 Word Occurrences:")
	print(str(freqDic100Len)+ " words occuring 5 or more times, or " + str(round((100*over100),2)) + "% of the total")
	print(" ")
	print(freqDic100)
	print("---------------------")
if freqDic5Len == 0 and freqDic10Len == 0 and freqDic25Len == 0 and freqDic50Len == 0 and freqDic100Len == 0:
	print("###############")
	print(" >= 1 Word Occurences: ")
	print(wordFreqDic)
	print("---------------------")

######PLOTS###########
# plot function 
def plotWords(wordDic):
	plt.plot(*zip(*sorted(wordDic.items())))
	plt.show()

if freqDic5Len != 0:
	plotWords(freqDic5)
if freqDic10Len != 0:
	plotWords(freqDic10)
if freqDic25Len != 0:
	plotWords(freqDic25)
if freqDic50Len != 0:
	plotWords(freqDic50)
if freqDic100Len != 0:
	plotWords(freqDic100)

