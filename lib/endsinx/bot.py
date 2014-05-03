import random
import re
import simplejson
import time
import tweepy

from . import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def make_used_unused():
    words = open('words')
    regex = re.compile(r'^[a-z]*x$')
    lines = [line.strip() for line in words.readlines() if regex.match(line)]
    unused = open('unused', 'w')
    unused.write(simplejson.dumps(lines))
    used = open('used', 'w')
    used.write(simplejson.dumps([]))


def get_word():
    unused = open('unused', 'r')
    words = simplejson.loads(unused.read())
    if not words:
        raise SystemExit
    word = words[random.randint(0, len(words) - 1)]
    words.remove(word)
    unused = open('unused', 'w')
    #unused.write(simplejson.dumps(words))

    used = open('used', 'r')
    used_words = simplejson.loads(used.read())
    used_words.append(word)
    used = open('used', 'w')
    #used.write(simplejson.dumps(used_words))

    return word


class Bot(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def do_bot_things(self):
        #make_used_unused()
        print 'sleeping x hours'
        #time.sleep(60*60*24)
        while True:
            tweet = get_word()
            print tweet
            #self.api.update_status(tweet)
            print 'sleeping 24 hours'
            time.sleep(60*60*24)
            #time.sleep(1)

        #time.sleep(3600) # Sleep for 1 hour



