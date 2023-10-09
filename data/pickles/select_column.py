from datetime import datetime
import re
import pandas as pd
import pickle

with open('ekphrasis_data.pkl', 'rb') as file:
    tweets_df = pickle.load(file)

tweets_df = tweets_df[['tweet_id', 'text', 'tokenized_text', 'created_at']]

# Replace date column with days after May 1, 2020 (start of the dataset)
def days_after(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    start = datetime(2020,5,1)
    return (date_obj - start).days

tweets_df['days_after'] = tweets_df['created_at'].apply(days_after)

hashtag_pattern = re.compile('<hashtag>(.*?)</hashtag>')

tweets_df['parsed_hashtags'] = tweets_df['tokenized_text'].str.findall(hashtag_pattern)

tweets_df['hashtags'] = tweets_df['parsed_hashtags'].apply(lambda list: [hashtag.replace(" ", "") for hashtag in list])

tweets_df = tweets_df[['tweet_id', 'hashtags', 'days_after']]

with open('id_hashtags_days.pkl', 'wb') as output:
    pickle.dump(tweets_df, output)