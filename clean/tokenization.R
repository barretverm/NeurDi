#### TOKENIZATION TEST SCRIPT 

library(tidyverse)
library(magrittr)

setwd('~/UCF/Research/Neurodiversity/NeurDi/data/2022-Apr-30')
data <- read.csv('2022-Apr-30.csv', header=T)

names(data)
# making sure all data is from April 30
head(data$created_at)
tail(data$created_at)


unique(data$lang)
# there are different languages listed -- checking them out
# [1] "en"  "qme" "ja"  "es"  "in"  "ro"  "und" "de"  "qht" "zxx" "fr" 

qme <- data %>% filter(lang=='qme')
qme$text
# qme appears to be in english?

ja <- data %>% filter(lang=='ja')
ja$text
# definitely japanese - need to omit

es <- data %>% filter(lang=='es')
es$text
# there's only one, and it's suspect. bot?

IN <- data %>% filter(lang=='in')
IN$text
# not in english

ro <- data %>% filter(lang=='ro')
ro$text
# only one, seems suspect maybe

und <- data %>% filter(lang=='und')
und$text
# just a few english hash tags

de <- data %>% filter(lang=='de')
de$text
# one tweet, in german

qht <- data %>% filter(lang=='qht')
qht$text
# 4 results, just hash tags

zxx <- data %>% filter(lang=='zxx')
zxx$text
# one sketchy tweet

fr <- data %>% filter(lang=='fr')
fr$text
# french

## I think it's safe to include only english ('en')
data %<>% filter(lang=='en')
