############## BASIC EXPLORATION WITH TIDYTEXT ###############

library(tidytext)
library(tidyverse)

  # using the smart lexicon from tidytest stop_words
  # stop_words <- get_stopwords(language = "en", source = "smart")

setwd("~/Research/text_mining/NeurDi_git/NeurDi/preprocesing_diagnostics")
df <- read.csv("2021-Mar-preprocessed.csv", 
stringsAsFactors=F)

# March 2021 has a spam bot "TheCrytoWow" - this may not generalize, but I'm filter out below


stop_words <- read.csv("n-gram_stop_word_list.csv")

df.tidy <- df %>%  
    unnest_tokens(word, text) %>% 
    filter()
    anti_join(stop_words)
