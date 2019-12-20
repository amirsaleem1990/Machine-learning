library(tm)

# Create corpus
corpus = VCorpus(VectorSource(emails$email))

# Pre-process data
corpus = tm_map(corpus, tolower)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords("english"))
corpus = tm_map(corpus, stemDocument)

