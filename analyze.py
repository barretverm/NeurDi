import gensim.corpora as corpora
import matplotlib.pyplot as plt
import pandas as pd
import string

from collections import Counter
from gensim.models import LdaModel
from clean.tokenization import *
from pathlib import Path
from wordcloud import WordCloud

def word_cloud(year, month):
    path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
    file = Path(path)
    if not file.exists():
        return
    
    print('Analyzing ' + year + '-' + month)
    tweet_df = pd.read_csv(path)
    
    tweet_df['tokenized_text'] = tweet_df['tokenized_text'].str.split()
    tweets = [tweet for tweet in tweet_df['tokenized_text'] if isinstance(tweet, list)]
    tokens = [word for tweet in tweets for word in tweet]

    word_freq = Counter(tokens)

    # Generate wordcloud and save image
    wordcloud = WordCloud(width=800, height=400, max_words=200,
                          background_color='white').generate_from_frequencies(word_freq)

    graphic_path = Path('graphics/' + year + '/' + year + '-' + month + '.png')
    graphic_path.parent.mkdir(parents=True, exist_ok=True)
    wordcloud.to_file(graphic_path)

def full_word_cloud():
    tweets = []

    # Combine tweets from all months
    for year in ['2020', '2021', '2022', '2023']:
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            # Read in data
            path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
            file = Path(path)
            if not file.exists():
                break
            tweet_df = pd.read_csv(path)

            # Retokenize space-separated token strings
            tweet_df['tokenized_text'] = tweet_df['tokenized_text'].str.split()
            tweets.extend([tweet for tweet in tweet_df['tokenized_text'] if isinstance(tweet, list)])
    
    tokens = [word for tweet in tweets for word in tweet]

    word_freq = Counter(tokens)

    # Generate wordcloud and save image
    wordcloud = WordCloud(width=800, height=400, max_words=200,
                          background_color='white').generate_from_frequencies(word_freq)

    graphic_path = Path('graphics/allmonths.png')
    graphic_path.parent.mkdir(parents=True, exist_ok=True)
    wordcloud.to_file(graphic_path)

def lda(year, month):
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

    # Initialize and train model
    num_topics = 5
    num_passes = 10
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=num_passes)

    # Save results
    path = Path('analysis/lda_results/' + year + '/' + year + '-' + month + '.txt')
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        f.write(f"Num_topics: {num_topics}. Num_passes: {num_passes}\n\n")
        for topic_id in range(num_topics):
            f.write(f"Topic {topic_id + 1}:\n")
            f.write(lda_model.print_topic(topic_id))
            f.write("\n\n")

def full_lda(num_topics, num_passes):
    tweets = []

    # Combine tweets from all months
    print("Collecting data")
    for year in ['2020', '2021', '2022', '2023']:
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            # Read in data
            path = 'clean/'+ year + '/' + year + '-' + month + '.csv'
            file = Path(path)
            if not file.exists():
                break
            tweet_df = pd.read_csv(path)

            # Retokenize space-separated token strings
            tweet_df['tokenized_text'] = tweet_df['tokenized_text'].str.split()
            tweets.extend([tweet for tweet in tweet_df['tokenized_text'] if isinstance(tweet, list)])

    dictionary = corpora.Dictionary(tweets)
    # Document term frequency
    corpus = [dictionary.doc2bow(tokens) for tokens in tweets]

    # Initialize and train model
    print("Performing LDA...")
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=num_passes, per_word_topics=True)

    # Save results
    path = Path('analysis/full_lda_results.txt')
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        f.write(f"Num_topics: {num_topics}. Num_passes: {num_passes}\n\n")
        for topic_id in range(num_topics):
            f.write(f"Topic {topic_id + 1}:\n")
            f.write(lda_model.print_topic(topic_id))
            f.write("\n\n")

clean_all()
full_lda(10, 10)
# full_word_cloud()