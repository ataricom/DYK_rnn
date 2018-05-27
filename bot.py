import random
import tweepy
from credentials import *
from time import sleep

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

dyk_text=open('dyk.txt','r')
with dyk_text as d:
    facts=d.readlines()
    
def loop():
    for line in facts:
#        fact=random.choice(line)
        try:
            print(line)
            api.update_status(line)
            sleep(3600)

# echo error and delay 2 seconds instead of interrupting and halting
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)        

while True:
    loop()

    
    
