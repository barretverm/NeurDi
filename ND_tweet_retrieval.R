### TWITTER MINING FOR NEURODIVERSITY

library(academictwitteR)


### SET TWITTER BEARER IN .Renviron FILE AND RESTART .rs.restartR()
set_bearer()
### AFTER RESTART, GET BEARER
get_bearer()

### QUERY THE TWITTER API - CHANGE VALUES FOR SUBSEQUENT SEARCHES/RETRIEVALS

### CONDUCT PRELIMINARY COUNTS TO GUAGE N FOR TWEET RETRIEVAL
# NOTE: N IS THE NUMBER OF UNITS IN GRANULARITY. FOR EXAMPLE, IF "MONTHS",
# THEN JANUARY THROUGH FEBRUARY IS N = 2. IF 31 DAYS, THEN GRANULARITY = 'DAY',
# AND N = 31
count <- count_all_tweets(
  query= 'neurodiversity', '#neurodiversity',
  start_tweets = '2021-02-01T00:00:00Z',
  end_tweets = '2021-05-01T00:00:00Z',
  bearer_token = get_bearer(),
  n= 60,
  granularity= 'day',
  verbose= T,
  lang= 'en',
  remove_promoted= T
)

### TWEET RETRIEVAL
tweets <- get_all_tweets(
  query= 'neurodiversity', '#neurodiversity',
  start_tweets = '2021-11-01T00:00:00Z',
  end_tweets = '2022-01-01T00:00:00Z',
  bearer_token = get_bearer(),
  n = 50000,
  data_path = '~/data/Twitter_API/neurodiversity_data/110121-010123',
  export_query = T,
  bind_tweets = F,
  page_n = 500,
  context_annotations = T,
  verbose = T,
)


### BINDING TWITTER JSON FILES
library(tidyverse)
library(tidyselect)


### SPECIFY FOLDER DIRECTORY. THIS FUNCTION WILL BIND THE JSON FILES
### CONTAINED WITHIN THE FOLDER.
AUG.NOV.2020 <- bind_tweets(
  '~/data/Twitter_API/neurodiversity_data/2020-Aug-31_2020-Nov-30', 
  verbose = T, 
  output_format = 'tidy')


### VERIFY DATA. LOOK USE created_at COLUMN TO MAKE SURE YOU HAVE THE 
### CORRECT RANGE IN TIME
glimpse(AUG.NOV.2020)
tail(AUG.NOV.2020$created_at)


### EXPORT CSV
setwd()
write.csv(AUG.NOV.2020, '2020-Aug-31_2020-Nov-30.csv')
