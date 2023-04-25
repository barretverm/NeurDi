from nltk import TweetTokenizer
from pathlib import Path
import re
import pandas as pd

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

    # remove retweets
    tweets_df = tweets_df[tweets_df['sourcetweet_type']!='retweeted']

    tweets_df = tweets_df[['tweet_id', 'user_username', 'author_id', 'user_name',
                        'text', 'created_at', 'in_reply_to_user_id',
                        'user_created_at', 'user_description', 'user_location',
                        'retweet_count', 'like_count', 'quote_count',
                        'user_followers_count','user_following_count', 'sourcetweet_type']]

    # Tokenizer
    tk = TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=True)

    tweets_df['tokenized_text'] = tweets_df['text'].apply(tk.tokenize)

    # Remove urls
    url_pattern = re.compile('https:\/\/t.co\/\w*')
    def remove_url(tokenized_tweet):
        return [word for word in tokenized_tweet if not url_pattern.match(word)]

    tweets_df['tokenized_text'] = tweets_df['tokenized_text'].apply(remove_url)

    # Export cleaned df to csv
    filepath = Path('clean/'+ year + '/' + year + '-' + month + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tweets_df.to_csv(filepath)

for year in ['2020', '2021', '2022', '2023']:
    for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        clean(year, month)