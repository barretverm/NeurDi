import gensim.downloader as downloader
from gensim import models

glove = downloader.load("glove-wiki-gigaword-100")

# Positive keywords and negative keywords
positive = ['supervisor']
negative = []

# Query the model
similar_words = glove.most_similar(
    positive = positive,
    negative = negative,
    topn = 50
)

output_file = 'test.txt'

# Write the similar words and their similarity scores to the output file
with open(output_file, 'w') as f:
    for word, score in similar_words:
        f.write(f"{word}: {score}\n")
