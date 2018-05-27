## Twitter bot v0.2a
## Switched from char-rnn to textgenrnn for "dyk" generation
## Generates text on demand, rather than creating a file in advance and posting item by item
## Consolidated modeling, replacing '...' with 'Did you know' and posting with one py file
## Creates list of posted tweets for review

import tweepy
from credentials import *
from textgenrnn import textgenrnn
from time import sleep

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

tg=textgenrnn('dyk_weights.hdf5')
out=open('random.txt', 'a')

def dyk():
    dyk=tg.generate(temperature=0.8, return_as_list=True)
    dyk=dyk[0]
    return dyk

def loop():
    a=dyk()
    b=len(a)-1      #Be careful with len(). a[b] gives overflow because length is always nonzero. MUST subtract 1 to avoid overflow error
    a='Did you know'+a[3:b]
    
    if a[b]=='?':   #If end of generated line = ? then line feed
        a=a+'\n'
    else:           #Otherwise, add ? and then line feed
        a=a+'?\n'
    
    out.write(a)
    out.flush()

    try:
        api.update_status(a)
        sleep(3600)
    except tweepy.TweepError as e:
        print(e.reason)
        out.write(e.reason)
        out.flush()
        sleep(1)
while True:
    loop()
    
## TODO
## Timestamp output txt file
## Markov chain? Maybe randomly choose which form of generation to use
