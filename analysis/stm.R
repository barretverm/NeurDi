library(tidytext)
library(tm)
library(stm)

# unpackage data from cleaned csv file
colClasses <- c("integer", "character", "logical")
cleanedData <- read.csv("prepped/2023/2023-Mar.csv", header = TRUE, colClasses=colClasses)

# Rename for processing
colnames(cleanedData) <- c("doc_id", "text", "is_after")

# stm requires metadata in df or matrix format
metadata <- cleanedData[,c('is_after', 'doc_id')]

# Prep corpus
out <- textProcessor(documents = cleanedData$text, metadata = metadata)

# Analyze appropriate number of topics (K)
# set.seed(2023)
# stm_search <- searchK(documents = out$documents, vocab = out$vocab, K = 2:30,
#                       init.type = "Spectral", data = out$meta, verbose=FALSE)


# Run STM
stm <- stm (documents = out$documents, vocab = out$vocab, K = 10, data = out$meta)
