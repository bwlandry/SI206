# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


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



for tweet in tweets:
	
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)



print("Average subjectivity is")
print("Average polarity is")
