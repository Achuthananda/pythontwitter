# https://realpython.com/twitter-bot-python-tweepy/
import re,os
import tweepy,twitter
from tweepy import OAuthHandler,API,Stream
from configparser import ConfigParser
import time
import random
import os
import sys



class MyListener(tweepy.Stream):
    def on_status(self, status):
        print(status.text)
        print('*'*80)
        
    def on_error(self, status):
        print(status)
        return True


consumer_key='Eg3VhBh1NM0j$$$$ugs6baReWBhcBxyz'
consumer_secret='ZtSbqdSSqhu^^gS80Oy0OXGAIWmCP75DlrX5s57LxyzrX88qtwg1ghexyz'
access_token_key='1237004240997892skjsdkasd098-H2jqYueh1ReEL8UH5xyzz8ltYgUjXKkf5J'
access_token_secret='2EGdt***yl3YYf9jkk0bUPAszy23chMXXV149pQXjdxK6npTPlWR1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)
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


def getStream(topicArray):
    twitter_stream = MyListener(consumer_key,consumer_secret,access_token_key, access_token_secret)
    twitter_stream.filter(track=topicArray)


topics = ['PuneetRajkumar','Modi','Virat']
getStream(topics)

'''
getAllTweets()
for info in alltweets:
    likeTweet(info.id)
'''
