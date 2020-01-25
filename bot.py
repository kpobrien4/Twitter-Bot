import tweepy
from keys import *
import sys
import time
from random import random

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # tweet every 15 seconds

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def hello():
    return("Hello " + str(random()))


while True:
    print("Tweeting...")
    hello = hello()
    api.update_status(hello)
    time.sleep(INTERVAL)
