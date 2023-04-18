from gensim.corpora.dictionary import Dictionary
from nltk import TweetTokenizer
from pathlib import Path
import pandas as pd

def analyze(year, month):
    path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
    tweet_df = pd.read_csv('clean/2023/2023-Mar.csv')

    tk = TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=True)
    # counter = Counter()
    tweet_df['tokenized_text'] = tweet_df['text'].apply(tk.tokenize)
    # tweets_df['tokenized_text'].apply(counter.update)
    # counter.update(tweets_df['sourcetweet_type'])
    # common = {elem:count for elem, count in counter.items() if count > 1000}
    # print(counter)

    dictionary = Dictionary(tweet_df['tokenized_text'])
    corpus = [dictionary.doc2bow(tweet) for tweet in tweet_df['tokenized_text']]
    print(corpus[4][:10])

analyze('2023', 'Mar')