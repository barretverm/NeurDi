import pandas as pd
import pickle

from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

# Load in dataset
with open('rawdata.pkl', 'rb') as input:
    tweets_df = pickle.load(input)

# keep english
tweets_df = tweets_df[tweets_df['lang']=='en']

# Remove retweets
tweets_df = tweets_df[tweets_df['sourcetweet_type']!='retweeted']

# Set preprocessor/tokenizer options
text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'percent', 'money', 'phone', 'user',
        'time', 'url', 'date', 'number'],
    # terms that will be annotated
    annotate={"hashtag", "allcaps", "elongated", "repeated",
        'emphasis', 'censored'},
    fix_html=True,  # fix HTML tokens
    
    # corpus from which the word statistics are going to be used 
    # for word segmentation and spell correction
    segmenter="twitter", 
    corrector="twitter", 
    
    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=False,  # spell correction for elongated words
    
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    
    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionary.
    dicts=[emoticons]
)

# Preprocess and tokenize
tweets_df['tokenized_text'] = tweets_df['text'].apply(text_processor.pre_process_doc)
tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(" ".join)

with open('ekphrasis_data.pkl', 'wb') as output:
    pickle.dump(tweets_df, output)