#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='JKgobPULfxXmAtVHxIPMzYNNw',
consumer_secret='f4HTr6cfpWPQpLoQUeO40rPjeCxDKhp5jeMYNdVy8agMOIy4PZ',
access_token='1026291499997122560-P2im4w9DcGaOzJI9guCk7lop7jAnC8', 
access_token_secret='IHJyRMOFYHE639dA9sHmzqX8YlZ9GZPe7N1Q7sPsnYeql'
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
