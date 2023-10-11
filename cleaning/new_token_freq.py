import pandas as pd
import pickle
from collections import defaultdict, Counter
from nltk import word_tokenize
from nltk.tokenize import MWETokenizer

'''
# Import custom dictionaries
def load_custom_dicts_as_df(path):
    
    df = pd.DataFrame()
    
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                category = line[2:]
                df[category] = None
                counter = 0
            else:
                df.at[counter, category] = line
                counter += 1
    return df

lockdown = load_custom_dicts_as_df('lockdown_dict.txt')
lockdown.to_csv('lockdown_dict.csv')

supervisor = load_custom_dicts_as_df('supervisor_dict.txt')
supervisor.to_csv('supervisor_dict.csv')

work = load_custom_dicts_as_df('work_dict.txt')
work.to_csv('work_dict.csv')
'''

# Load in dataset
with open('pickles/rawdata.pkl', 'rb') as input:
    tweets_df = pickle.load(input)
    
# keep english
tweets_df = tweets_df[tweets_df['lang']=='en']

# Remove retweets
tweets_df = tweets_df[tweets_df['sourcetweet_type'] != 'retweeted']

# Only keep columns of interest
tweets_df = tweets_df[['tweet_id', 'text']]
