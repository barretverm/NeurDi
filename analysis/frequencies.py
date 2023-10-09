import matplotlib.pyplot as plt
import pandas as pd
import pickle

from collections import Counter
from datetime import datetime, timedelta

with open('pickles/id_hashtags_days.pkl', 'rb') as output:
    df = pickle.load(output)
    
# Create an empty Counter to store word frequencies
word_frequency = Counter()

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    
    tags = row['hashtags']

    # Update the word frequencies for the corresponding time period
    time_period = row['days_after']
    word_frequency.update({(tag, time_period): 1 for tag in tags})


# Plot the frequency graph for a given hashtag

target_hashtag = 'neurodiversitycelebrationweek'

# Extract the frequencies for the target token over time
token_frequencies = [(time, freq) for (word, time),
                    freq in word_frequency.items() if word == target_hashtag]

# Sort the data by time
token_frequencies.sort(key=lambda x: x[0])

# Separate time and frequency into separate lists
time_periods, frequencies = zip(*token_frequencies)

# Convert time_periods to actual dates
start_date = datetime(year=2020, month=5, day=1)
dates = [start_date + timedelta(days=int(time)) for time in time_periods]

# Create a line graph with real dates on the x-axis
plt.figure(figsize=(20, 8))
plt.hist(dates, bins=152, edgecolor='k', alpha=0.7) # each bin is a week
plt.title(f'Frequency Distribution of #{target_hashtag} Over Time')
plt.xlabel('Date')
plt.ylabel('Frequency')

plt.savefig('nd_week_freq.png')
