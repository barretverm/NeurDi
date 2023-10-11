import matplotlib.pyplot as plt
import pandas as pd
import pickle

from collections import Counter
from datetime import datetime

with open('data/pickles/custom.pkl', 'rb') as output:
    df = pickle.load(output)

# Convert to actual dates
df['date'] = df['created_at'].apply(
    lambda time: datetime.date(datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ"))
)

# Compile list of custom_tokens
work = pd.read_csv('custom_lists/work_dict.csv') 
lockdown = pd.read_csv('custom_lists/lockdown_dict.csv')
supervisor = pd.read_csv('custom_lists/supervisor_dict.csv')
full = pd.concat([work, lockdown, supervisor])

custom_tokens = []
for _, tokens in full.items():
    for token in tokens:
        if isinstance(token, float):
                continue
        split = token.split()
        custom_tokens.append('_'.join(split))

# Initialize Counter for each date
date_counters = {}
for date in df['date'].unique():
    date_counters[date] = Counter()

i = 0
for index, row in df. iterrows():
    date = row['date']
    text = row['tokenized_text']
    filtered_text = [token for token in text if token in custom_tokens]
    token_counter = Counter(filtered_text)
    date_counters[date] += token_counter

out = pd.DataFrame.from_dict(date_counters, orient='index')

out.to_csv('custom_frequencies.csv')