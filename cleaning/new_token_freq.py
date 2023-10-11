import numpy as np
import pandas as pd
import pickle
import re
from collections import defaultdict, Counter
from datetime import datetime
from nltk import word_tokenize
from nltk.tokenize import MWETokenizer

# Load in dataset
with open('data/pickles/ekphrasis.pkl', 'rb') as input:
    tweets_df = pickle.load(input)

tweets_df = tweets_df[['tweet_id', 'text', 'tokenized_text', 'created_at']]

# Replace date column with days after May 1, 2020 (start of the dataset)
def days_after(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    start = datetime(2020,5,1)
    return (date_obj - start).days

tweets_df['days_after'] = tweets_df['created_at'].apply(days_after)

tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(
    lambda line: line.split(' ')
)

# Keep only 
pattern = re.compile('[A-Za-z]+')
tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(
    lambda tokens: [word for word in tokens if re.match(pattern, word)]
)

# Pull in custom dictionaries for token combinations with MWETokenizer
work = pd.read_csv('custom_lists/work_dict.csv')
lockdown = pd.read_csv('custom_lists/lockdown_dict.csv')
supervisor = pd.read_csv('custom_lists/supervisor_dict.csv')

multidict = []

for df in [work, lockdown, supervisor]:
    for _, terms in df.items():
        for term in terms:
            if isinstance(term, float):
                continue
            if len(term.split()) > 1:
                multidict.append(term.split())

mwe_tokenizer = MWETokenizer(multidict, separator='_')

# Use the tokenizer to combine multiword terms from the custom lists
tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(mwe_tokenizer.tokenize)

tweets_df = tweets_df[['tweet_id', 'tokenized_text', 'created_at']]

with open('data/pickles/custom.pkl', 'wb') as output:
    pickle.dump(tweets_df, output)