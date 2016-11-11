# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "355173887-zzfk7cj4AoGpBMb84DoAPYtrGvsWYwLcqcVdB7oc"
access_token_secret = "a5tmwDjcEckR3Uw5PFNRNaHCLrB84QN9IvYrQHvQXCEgH"
consumer_key = "RbeQJESDEnT18VhxPPF20hqF8"
consumer_secret = "FxE5bu3aBsQE869AVjjBZwsDJ2upOCw3Uq7h2KueKSeaJtDbFb"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)



tweet = tweepy.API(auth)

mystatus = "Posting this tweet with python for a class #UMSI-206 #Proj3"
tweet.update_with_media("/Users/Ben/Pictures/drill.jpg", status = mystatus )

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")