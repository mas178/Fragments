#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import random

QUOTES = [{'quote': item[0], 'name': item[1], 'language': item[2]} for item in [line.replace("\n", '').split("\t") for line in open('./quotes.txt', 'r')]]
QUOTES = ["{} by {} #{}".format(q['quote'], q['name'], q['language']) for q in QUOTES if q['name'] != '' and q['language'] != '' and q['quote'] != '']
QUOTES = [q for q in QUOTES if len(unicode(q, 'utf-8')) <= 140]
token = dict([tuple(line.replace("\n", '').split('=')) for line in open('./token.tsv', 'r')])
auth = tweepy.OAuthHandler(token['consumer_key'], token['consumer_secret'])
auth.set_access_token(token['access_token_key'], token['access_token_secret'])
tweepy.API(auth).update_status(status=random.choice(QUOTES))
