
import pandas as pd
import nltk
import tensorflow as tf



goodreads  = pd.read_csv('/finalgoodreads.csv')
nyt = pd.read_csv('/nyt_bestseller.csv')

## ok so goodreads = train data. 0 for don't like, would not like, 1 for could like, and likes.
## vector embedding for the sysnopsis





