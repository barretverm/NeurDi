bc = because
hr = human resources

exclude 2021, 2022 and 2023 from numbers being removed

there are a lot of duplicates - there are basically none among verified users. I'm going to use verified users
** "TheCryptoWow" is clearly a spam bot - going to remove

n = 11,904 before excluding non-verified users
n = 487 excluding non-verified

I'm going to run both verified and non-verifed

step_1 (the csv file includes non-verified): 
- exclude quoted and retweets
- exclude non-verified
- include english only

step_2 (the csv file includes non-verified): 
- remove links 
- remove duplicates (not removing for verified data set)
** I'm going to try removing all duplicate tweets that have 
5+ words that are the same and in the same order

step_3:
- lowercase

step_4: 
- remove hashtags and put in new column

step 5:
- remove tagged users and put in new column

step 6:
- contractions

step 7: 
- remove punctuation

step 8: 
- remove numbers

step 9: 
- lemmatize

step 10: 
- negations

step 11:
- stop words
** this is where things got messed up

step non-ver_revert
- reverting tidytext tokenized column into original format

ver-stop
- using tidytext to remove stop words

i used tidytext to remove stop words, but it converted it into a single-token-per-row format. i tried coverting it back (the revert csv's) but now there are less rows, and only two columns. 
- need to modify the stop words list - it contains words like "against"
