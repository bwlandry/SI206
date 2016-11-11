# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.



import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

    enc = file.encoding

    if enc == 'UTF-8':

        print(*objects, sep=sep, end=end, file=file)

    else:

        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)

        print(*map(f, objects), sep=sep, end=end, file=file)


import tweepy
import nltk
from textblob import TextBlob

# Unique code from Twitter
access_token = "355173887-zzfk7cj4AoGpBMb84DoAPYtrGvsWYwLcqcVdB7oc"
access_token_secret = "a5tmwDjcEckR3Uw5PFNRNaHCLrB84QN9IvYrQHvQXCEgH"
consumer_key = "RbeQJESDEnT18VhxPPF20hqF8"
consumer_secret = "FxE5bu3aBsQE869AVjjBZwsDJ2upOCw3Uq7h2KueKSeaJtDbFb"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search("Jay Cutler")

total_polarity = 0
total_sentiment = 0

for tweet in tweets:
	
	uprint(tweet.text)
	analysis = TextBlob(tweet.text)
	total_polarity += analysis.sentiment.polarity
	total_sentiment += analysis.sentiment.subjectivity
	uprint(analysis.sentiment)



print("Average subjectivity is", total_sentiment/len(tweets) )
print("Average polarity is", total_polarity/len(tweets))
