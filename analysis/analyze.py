from gensim.corpora.dictionary import Dictionary
from nltk import TweetTokenizer
from pathlib import Path
import pandas as pd

tweet_df = pd.read_csv('clean/2023/2023-Mar.csv')

tk = TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=True)
counter = Counter()

tweets_df['tokenized_text'] = tweets_df['text'].apply(tk.tokenize)
tweets_df['tokenized_text'].apply(counter.update)
counter.update(tweets_df['sourcetweet_type'])

common = {elem:count for elem, count in counter.items() if count > 1000}
print(counter)