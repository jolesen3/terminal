#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='Key',
consumer_secret='Key',
access_token='Key', 
access_token_secret='Key'
)
user = "@APPLEH4CKZ"
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
