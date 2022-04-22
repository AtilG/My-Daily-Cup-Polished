"""Twitter API"""
import os
import tweepy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def get_trends():
    """Gets top trending tags from twitter"""
    # assign the values accordingly
    consumer_key = os.getenv("TWITTER_KEY")
    consumer_secret = os.getenv("TWITTER_SECRET")
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # WOEID of the United States
    woeid = 23424977

    # getting authorization for our keys, then finding the trending topics
    trends = tweepy.API(auth).get_place_trends(id=woeid)
    trends = trends[0]["trends"]

    # This will find the top 5 trending topics
    trending_topics = []
    i = 0
    for trend in trends:
        trending_topics.append(trend["name"])
        i += 1
        if i == 5:
            break
    return trending_topics
