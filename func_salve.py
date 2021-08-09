import tweepy, time, random, threading

from os import environ


from func_global import *

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Responder salve

file_name_salve = 'salve/last_salve_id.txt'

def manda_salve():
    print('Respondendo salve...', flush=True)
    
    while True:
        time.sleep(10)

        last_seen_id_salve = retrieve_last_seen_id(file_name_salve)
        
        mentions = api.mentions_timeline(
                                since_id = last_seen_id_salve,
                                tweet_mode='extended')
            
        for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id_salve = mention.id
            store_last_seen_id(last_seen_id_salve, file_name_salve)
            
            if 'salve' in mention.full_text.lower():
                try:
                    print("Salve, cachorro do mangue")
                    api.update_status("@" + mention.user.screen_name + 
                                    " Salve, cachorro do mangue!", mention.id)
                except tweepy.TweepError as error:
                    if error.api_code == 187:
                        print('Erro: Salve já enviado!')  

p_manda_salve = threading.Thread(target = manda_salve)