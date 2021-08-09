import tweepy
import time
from os import environ

from tweepy.models import Status


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


tweet = api.get_status(id="1424473042894340096")
print(tweet.in_reply_to_status_id)

pai = tweet.in_reply_to_status_id
tweet_pai = api.get_status(id=pai)
print(tweet_pai.text + ' - ' + ' TWEET DO PAI ' )

# RESPONDE O TWEET FILHO COM O TEXTO EM MORSE
morse = tweet_pai.text

morse[0:3]


s =  '@vitor @luiza vitor'
while '@' in s:
    s.replace((s[s.find('@'):s.find(' ')+1]), '')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'vgs_studio' # Usuário

mentions = api.user_timeline(userID, 
                           tweet_mode = 'extended'
                           )

# MENÇÕES
for info in reversed(mentions[:100]):
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")