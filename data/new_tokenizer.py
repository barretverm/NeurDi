import pandas as pd

from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons
from pathlib import Path

def clean(year, month):
    
    csv_path = 'raw_data/' + year + '/' + year + '-' + month + '.csv'
    file = Path(csv_path)
    print(file)
    if not file.exists():
        print("Couldn't find files.")
        return

    print('Cleaning ' + year + '-' + month)

    # Read into df
    tweets_df = pd.read_csv(csv_path)

    # keep english
    tweets_df = tweets_df[tweets_df['lang']=='en']

    # Remove retweets
    tweets_df = tweets_df[tweets_df['sourcetweet_type']!='retweeted']
    
    # Remove unnecessary columns
    # tweets_df = tweets_df[['tweet_id', 'user_username', 'author_id', 'user_name',
    #                     'text', 'created_at', 'in_reply_to_user_id',
    #                     'user_created_at', 'user_description', 'user_location',
    #                     'retweet_count', 'like_count', 'quote_count',
    #                     'user_followers_count','user_following_count',
    #                     'sourcetweet_type']]
    tweets_df = tweets_df[['tweet_id','text']]
    
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

    # Export cleaned df to csv
    filepath = Path('sample/' + year + '-' + month + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tweets_df.to_csv(filepath)
    
clean('2023', 'Mar')