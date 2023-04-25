from gensim.corpora.dictionary import Dictionary
from nltk import TweetTokenizer
from pathlib import Path
import pandas as pd

def analyze(year, month):
    path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
    tweet_df = pd.read_csv('clean/2023/2023-Mar.csv')

# Cleaning and tokenization handled in tokenization.py

# counter = Counter()

# tweets_df['tokenized_text'].apply(counter.update)
# counter.update(tweets_df['sourcetweet_type'])

# common = {elem:count for elem, count in counter.items() if count > 1000}
# print(counter)