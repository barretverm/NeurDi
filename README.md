# Neurodiversity Tweet Text Analysis

The tweet data is has been retrieved/downloaded using R scripts. The data is stored in [raw_data](raw_data) in .csv format organized by year and month.

## Cleaning
The data is cleaned and tokenized by this python script: [clean/tokenization.py](clean/tokenization.py). Cleaning currently maintains the following data for each tweet.
- tweet_id
- user_username (Twitter handle)
- author_id
- user_name *(Profile Name)*
- text
- created_at
- in_reply_to_user_id
- user_created_at
- user_description
- user_location
- retweet_count
- like_count
- quote_count
- user_followers_count
- user_following_count
- sourcetweet_type
- **tokenized_text**

Retweets are discarded. Cleaned data is saved to [clean](clean) organized by year and month in .csv format. The tokenization/cleaning script can be adjusted and run again to overwrite the cleaned data. Tokenized_text is a new column with tweets prepared for bag-of-word analysis as a list of tokens.

## Analysis
NLP models and other analysis methods are scripted in [analysis](analysis).

**All filepaths in the code are relative to the root of the repository.*