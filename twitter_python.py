# https://realpython.com/twitter-bot-python-tweepy/
import re,os
import tweepy,twitter
from tweepy import OAuthHandler
from configparser import ConfigParser
import time
import random
import os


consumer_key='Hoa40a##***leY40wwyro4ZasdsadtVnNgB6e'
consumer_secret='FV60K4as##*****duyUWL1cadsasdJEesgF9NjnoV85fKYrDKsyNRfPqg4W8AfIBsh'
access_token_key='16279203aas5-EcjG$$$$$$**6WZDQSIg13nuEM1SsSKasIV3vWK2Rv0FHM7PU9'
access_token_secret='24Zt05jhadsadoCE###***VNupN826pqCvBWh7a11fcukTmGjGztRAVJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
twitterapi = twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,
                  access_token_key=access_token_key,access_token_secret=access_token_secret)


alltweets = []  
def getAllTweets(username):
    new_tweets = api.user_timeline(screen_name = username,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = username,count=20000,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print(f"...{len(alltweets)} tweets downloaded so far")


def likeTweet(tweetId):
    api.create_favorite(tweetId)


def getTrendingHashTags():
    hashtag_list = []
    hashtag_str = ""
    tags = api.trends_place(23424848) # 23424848 Corresponds to the Yahoo ID for India. Change this to the location that you require.
    for trend in tags[0]['trends']:
        if str(trend['tweet_volume']) != 'None' and trend['name'][0] == '#':
            hashtag_list.append(trend['name'])

    #index_list = []
    index_list = random.sample(range(0, len(hashtag_list)-1), 4)

    for i in index_list:
        hashtag_str = hashtag_str + ' ' + hashtag_list[i]

    return hashtag_str


def getMyfollowers():
    followers = twitterapi.GetFollowerIDs()
    print(len(followers))
    print(followers)

def getWhoIFollow():
    users = twitterapi.GetFriends()
    print('*'*80)
    for user in users:
        print("Name:",user.name)
        print("Screen Name:",user.screen_name)
        print("User ID:",user.id)
        print("Followers:",user.followers_count)
        print("Friends Count:",user.friends_count)
        print("Tweets:",user.statuses_count)
        print('*'*80)

def tweetImage(image_path,tweet_text):
    try:
        status = api.update_with_media(image_path, tweet_text)
        print("Posted the Tweet with Image")
    except Exception as e:
        print(e)

def tweetText():
    message = 'Hello World !! This is my first tweet from the API!!'
    try:
        status = api.PostUpdate(message)
    except Exception as e:
        print(e)

'''
getAllTweets()
for info in alltweets:
    likeTweet(info.id)
'''
