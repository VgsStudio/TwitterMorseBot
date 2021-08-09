from logging import exception
import time, random, threading
import tweepy


from os import environ, error

from func_global import *

from morse import *

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

file_name_salve = 'id.txt'

def morse():
    print('Procurando Tweets...', flush=True)
    
    while True:
        time.sleep(10)

        last_seen_id_salve = retrieve_last_seen_id(file_name_salve)
        
        mentions = api.mentions_timeline(
                                since_id = last_seen_id_salve,
                                tweet_mode='extended')
            
        for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.full_text + ' - ' + 'TWEET MENÇÃO') #ID DO TWEET
            last_seen_id_salve = mention.id
            store_last_seen_id(last_seen_id_salve, file_name_salve)

            try: 
                # PEGA O TXT DO TWEET ANTERIOR AO DELE (PAI)

                pai = mention.in_reply_to_status_id
                tweet_pai = api.get_status(id=pai)
                print(tweet_pai.text + ' - ' + ' TWEET DO PAI ' )
            except Exception as e:
                print('ERRO AO PEGAR O TWEET PAI')
                print(e)
            try:    
            # RESPONDE O TWEET FILHO COM O TEXTO EM MORSE
                morse = tweet_pai.text
                while '@' in morse:
                    morse.replace((morse[morse.find('@'):morse.find(' ')+1]), '')
                morse = encrypt(morse.upper())
            except Exception as e:
                print('ERRO AO TRADUZIR')
                print(e)
            try:
                api.update_status("@" + mention.user.screen_name + ' ' + morse, mention.id)
            except Exception as e:
                print('ERRO AO POSTAR')
                print(e)
            

p_morse = threading.Thread(target = morse)
