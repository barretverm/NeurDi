import matplotlib.pyplot as plt
import pandas as pd
import string
from collections import Counter
from gensim.corpora.dictionary import Dictionary
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

    wordcloud = WordCloud(width=800, height=400, max_words=200,
                          background_color='white').generate_from_frequencies(word_freq)

    graphic_path = Path('graphics/' + year + '/' + year + '-' + month + '.png')
    graphic_path.parent.mkdir(parents=True, exist_ok=True)
    wordcloud.to_file(graphic_path)
    
for year in ['2020', '2021', '2022', '2023']:
    for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        word_cloud(year, month)