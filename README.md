# NLP
Natural Language Processing with Python

![Image description](https://www.googleapis.com/drive/v3/files/10GstgLvY3YUyMD9wb8qHF1nQ4CQad73H?alt=media&key=AIzaSyDb-0FGRW1eS0pDUwvGJFM4SsxisP3j5rc)

Python scripts for web scraping and natural language processing.

1. healthNews.py shows how to calculate word frequency from a scraped web page
2. sentiment.py shows how to use VADER (Valence Aware Dictionary and sEntiment Reasoner)

########

NLTK Installation

$ pip install --user -U nltk

In Python Shell enable Natural Languge Toolkit Modules by entering commands and selecting in GUI

import nltk

nltk.download()

NOTE: If you have installed Python with anaconda, you may have issue on Mac where you get logged out when running matplotlb 

 in ~/.matplotlib/matplotlibrc just add the following line:

backend: qt5agg