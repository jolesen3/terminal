#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='tyTwbkgzKsB8RiPDupYLOjqjv',
consumer_secret='35jwaCJn64FwnAUD7OWDPG4peDtRqXPSC94Nzjhup0TF1rr99x',
access_token='1026291499997122560-gStQMjeCYcI7nUg94dGhAb8wZfTnex', 
access_token_secret='rW4UausNVyKz64cLthHTMx8vXWoDiz95gus8uYOjtNDRJ'
)
user = "@_AppleExpert"
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet()