import markovify
from twython import Twython
import random
import os

#the twitter stuff
APP_KEY = os.environ['TWITTER_APP_KEY']
APP_SECRET = os.environ['TWITTER_APP_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

with open("./sampleText/OntheOriginofSpecies-Darwin.txt") as f:
	eggs = f.read()

markov_eggs = markovify.Text(eggs)
print "markov_eggs"
print markov_eggs
def generateSentence():
    eggs_sentence = markov_eggs.make_sentence()

    if len(eggs_sentence) < 280:
    	result=eggs_sentence
        print ""
        print result
        print ""
        twitter.update_status(status=result)
    else:
        generateSentence()

generateSentence()
