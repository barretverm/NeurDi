from pathlib import Path
import re
import pandas as pd
import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
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
                        'user_followers_count','user_following_count', 'sourcetweet_type']]

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
    stop_words.add('')
    def remove_stop(tokenized_tweet):
        return [word for word in tokenized_tweet if not word.lower() in stop_words]
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_stop)

    # Rejoin the tokens for storage in a csv
    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(' '.join)

    # Export cleaned df to csv
    filepath = Path('clean/'+ year + '/' + year + '-' + month + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tweets_df.to_csv(filepath)

    # Fix misspellings
    # correct_words = words.words()

# clean('2023', 'Mar')
for year in ['2020', '2021', '2022', '2023']:
    for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        clean(year, month)
