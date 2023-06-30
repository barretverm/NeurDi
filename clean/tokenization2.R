#### TOKENIZATION TEST SCRIPT
library(tidyverse)
library(magrittr)

# set path import data ----
setwd('~/UCF/Research/Neurodiversity/NeurDi/raw_data/2020')
data <- read.csv('2020-Sep.csv', header = T)

names(data)
# making sure all data is from April 30
head(data$created_at)
tail(data$created_at)

unique(data$lang)

# there are different languages listed -- checking some out----
filter_lang <- function(df, lang_value) {
  filtered_df <- df %>% filter(lang == lang_value)
  return(filtered_df$text)
}

filter_lang(data, 'qme')
filter_lang(data, 'ja')
filter_lang(data, 'es')
filter_lang(data, 'in')
filter_lang(data, 'ro')
filter_lang(data, 'und')


## I think it's safe to include only english ('en')

data %<>% filter(lang=='en')
unique(data$lang)

# explore ----

# sort by tweet likes 
sort_likes <- data[order(data$like_count, decreasing=T),]
head(sort_likes$like_count, 10)
head(sort_likes$text)

# sort by retweets
sort_retweets <- data[order(data$retweet_count, decreasing = T),]
head(sort_retweets$retweet_count, 10)
head(sort_retweets$text)


# let's try march (ND awareness week)
setwd('~/UCF/Research/Neurodiversity/NeurDi/raw_data/2023')
data <- read.csv('2023-Mar.csv', header=T)

sort_likes <- data[order(data$like_count, decreasing=T),]
head(sort_likes$like_count, 10)
head(sort_likes$text)

# export top liked tweets
export <- head(subset(sort_likes, select=c(text, like_count, retweet_count)), 30)
write.csv(export, 'Mar-Top-Liked.csv')
glimpse(export)
