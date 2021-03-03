import tweepy
from tweepy import OAuthHandler
from tweepy import API

consumer_key = 'b9jpXUoMtEF0NTTmY92WmXFLH'
consumer_secret = 'nEu5t2CS0NLRyf1UWKlbFl3w3fltE0nO2sj0dvdv3gGCMW3jAU'
access_token = '1359485831820570625-bk80Hz4j6tOoDw37RtEp4JjzIko2HU'
access_secret = 'm19y7BXfBajQDneMYcIMWXdkuaMZRuj5iirUjqrOSwRUR'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

def search(query):
    api = tweepy.API(auth)
    max_tweets = 10
    response = api.search(q=query, count=max_tweets)

    return [tweet._json for tweet in response]
    
