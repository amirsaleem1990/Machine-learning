library(tm)

# Create corpus
corpus = VCorpus(VectorSource(emails$email))

# Pre-process data
corpus = tm_map(corpus, tolower)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords("english"))
corpus = tm_map(corpus, stemDocument)


# Create matrix
dtm = DocumentTermMatrix(corpus)

# Remove any <token> does not appear at least 3% documents
dtm = removeSparseTerms(dtm, 0.97)

# Create data frame
labeledTerms = as.data.frame(as.matrix(dtm))

# Add in the outcome variable
labeledTerms$responsive = emails$responsive

