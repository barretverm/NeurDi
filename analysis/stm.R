library(tidytext)
library(tm)
library(stm)

# unpackage data from cleaned csv file
colClasses <- c("integer", "character", "character")
cleanedData <- read.csv("prepped/2023/2023-Mar.csv", header = TRUE, colClasses=colClasses)

# Rename for processing
colnames(cleanedData) <- c("doc_id", "text", "is_after")

# stm requires metadata in df or matrix format
metadata <- cleanedData[,c('is_after', 'text')]

# Prep corpus
out <- textProcessor(documents = cleanedData$text, metadata = metadata)

# Analyze appropriate number of topics (K)
# set.seed(2023)
# K<-c(5,10,15,20)
# stm_search <- searchK(documents = out$documents, vocab = out$vocab, K = 5:20,
#                       init.type = "Spectral", data = out$meta, verbose=TRUE)

# Run STM
# stm_5 <- stm (documents = out$documents, vocab = out$vocab,  K = 5,data = out$meta, prevalence=~is_after, emtol=0.0001)
# stm_10 <- stm (documents = out$documents, vocab = out$vocab,  K = 10, data = out$meta, prevalence=~is_after, emtol=0.0001)
stm_15 <- stm (documents = out$documents, vocab = out$vocab,  K = 15, data = out$meta, prevalence=~is_after, emtol=0.00005)
# stm_20 <- stm (documents = out$documents, vocab = out$vocab,  K = 20, data = out$meta, prevalence=~is_after, emtol=0.0001)

# Display topics 1-30's 10 highest ranked words
# labelTopics(stm, topics = 1:30, n = 10)

varEffects <- estimateEffect(1:2 ~is_after, stm_15, out$meta)

save.image('stm_anaylsis5.RData')