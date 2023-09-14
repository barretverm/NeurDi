import gensim.corpora as corpora
import re
import pandas as pd
import nltk
import string

nltk.download('stopwords')
from nltk.corpus import stopwords
from pathlib import Path
from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS
# from nltk.stem import WordNetLemmatizer

def clean(year, month):
    csv_path = 'raw_data/' + year + '/' + year + '-' + month + '.csv'
    file = Path(csv_path)
    if not file.exists():
        return

    print('Cleaning ' + year + '-' + month)

    # Read into df
    tweets_df = pd.read_csv(csv_path)

    # keep english
    tweets_df = tweets_df[tweets_df['lang']=='en']

    # Remove retweets and unnecessary columns
    tweets_df = tweets_df[tweets_df['sourcetweet_type']!='retweeted']
    tweets_df = tweets_df[['tweet_id', 'user_username', 'author_id', 'user_name',
                        'text', 'created_at', 'in_reply_to_user_id',
                        'user_created_at', 'user_description', 'user_location',
                        'retweet_count', 'like_count', 'quote_count',
                        'user_followers_count','user_following_count',
                        'sourcetweet_type']]

    # Tokenizer
    tk = nltk.TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=True)
    tweets_df['tokenized_text'] = tweets_df['text'].apply(tk.tokenize)

    # Remove urls
    url_pattern = re.compile('https:\/\/t.co\/\w*')
    def remove_url(tokenized_tweet):
        return [word for word in tokenized_tweet if not url_pattern.match(word)]
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_url)

    # Collect hashtags
    hashtag_pattern = re.compile('#\S*')
    def keep_hashtags(tokenized_tweet):
        return [word for word in tokenized_tweet if hashtag_pattern.match(word)]
    def remove_hashtags(tokenized_tweet): 
        return [word for word in tokenized_tweet if not hashtag_pattern.match(word)]
    tweets_df['hashtags'] = tweets_df['tokenized_text'].apply(keep_hashtags)
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_hashtags)

    # Strip punctuation
    exclist = string.punctuation + string.digits
    table_ = str.maketrans('', '', exclist)
    def strip_punct(tokenized_tweet):
        return [word.translate(table_) for word in tokenized_tweet]
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(strip_punct)
    
    # Collect and remove non-words
    word_pattern = re.compile('[A-Za-z]+')
    def collect_punct(tokenized_tweet):
        return [word for word in tokenized_tweet if not word_pattern.match(word)]
    def remove_punct(tokenized_tweet):
        return [word for word in tokenized_tweet if word_pattern.match(word)]
    tweets_df['punctuation'] = tweets_df['tokenized_text'].apply(collect_punct)
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_punct)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    # Topic specific stopwords
    extras = ['neurodiverse', 'neurodiversity', 'neurodivergent',
              'week', 'th', '']
    stop_words.update(extras)
    def remove_stop(tokenized_tweet):
        return [word for word in tokenized_tweet if not word.lower() in stop_words]
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_stop)

    # Rejoin the tokens for storage in a csv
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(' '.join)

    # Export cleaned df to csv
    filepath = Path('clean/'+ year + '/' + year + '-' + month + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tweets_df.to_csv(filepath)

def clean_all():        
    for year in ['2020', '2021', '2022', '2023']:
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            clean(year, month)

# Not currently in use
def bigrams(month, year):
    # Read in data
    path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
    file = Path(path)
    if not file.exists():
        return
    print('Analyzing ' + year + '-' + month)
    tweet_df = pd.read_csv(path)

    # Retokenize space-separated token strings
    tweet_df['tokenized_text'] = tweet_df['tokenized_text'].str.split()
    tweets = [tweet for tweet in tweet_df['tokenized_text'] if isinstance(tweet, list)]

    dictionary = corpora.Dictionary(tweets)
    # Document term frequency
    corpus = [dictionary.doc2bow(tokens) for tokens in tweets]

    bigram = Phrases(tweets, min_count=3, threshold=10)

clean_all()