#### TOKENIZATION TEST SCRIPT 
library(tidyverse)
library(magrittr)

# set path import data ----
setwd('~/UCF/Research/Neurodiversity/NeurDi/raw_data/2020')
data <- read.csv('2020-Sep.csv', header=T)

names(data)
# making sure all data is from April 30
head(data$created_at)
tail(data$created_at)

unique(data$lang)
# there are different languages listed -- checking some out----

qme <- data %>% filter(lang=='qme')
qme$text

ja <- data %>% filter(lang=='ja')
ja$text

es <- data %>% filter(lang=='es')
es$text

IN <- data %>% filter(lang=='in')
IN$text

ro <- data %>% filter(lang=='ro')
ro$text

und <- data %>% filter(lang=='und')
und$text

de <- data %>% filter(lang=='de')
de$text

qht <- data %>% filter(lang=='qht')
qht$text

zxx <- data %>% filter(lang=='zxx')
zxx$text

fr <- data %>% filter(lang=='fr')
fr$text

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
