import re
import csv
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from contextlib import suppress
import time
import twitter
import json


class TwitterExperiment(object):
    def __init__(self):
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        try:

            self.auth = OAuthHandler(consumer_key, consumer_secret)

            self.auth.set_access_token(access_token, access_token_secret)

            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def user_Tweets(self, users):
        acc_list = users[0:]
        # return acc_list
        tws = []
        tws_list = []
        if len(acc_list) > 0:
            for target in acc_list:
                print("Getting data for " + target)
                item = self.api.get_user(target)
                #print("name: " + item.name)
                #print("screen_name: " + item.screen_name)
                #print("description: " + item.description)
                #print("statuses_count: " + str(item.statuses_count))
                #print("friends_count: " + str(item.friends_count))
                #print("followers_count: " + str(item.followers_count))
                no_of_tweets = item.statuses_count
                #print("statuses count =", no_of_tweets)
                tw = self.api.user_timeline(target)
                tws.append(tw)
            tws_list.append(tws)

    def user_Tweets_Ids(self, users, ids):
        # acc_list=users[0:]
        acc_list = [users]
        # return acc_list
        tws = []
        tws_list = []
        if len(acc_list) > 0:
            j = 0
            for target in acc_list:
                print("Getting data for " + target)
                item = self.api.get_user(target)
                #print ("\n", target)
                #print("\n name: " + item.name)
                #print("\n screen_name: " + item.screen_name)
                #print("description: " + item.description)
                #print("\n statuses_count: " + str(item.statuses_count))
                #print("\n friends_count: " + str(item.friends_count))
                #print("\n followers_count: " + str(item.followers_count))
                no_of_tweets = item.statuses_count
                #print("statuses count =", no_of_tweets)
                tw = self.api.user_timeline(target, max=ids[j], count=10)
                tws.append(tw)
                j = j+1

            # tws_list.append(tws)

        account_created_date = item.created_at
        delta = datetime.utcnow() - account_created_date
        account_age_days = delta.days
        print("Account age (in days): " + str(account_age_days))
        if account_age_days > 0:
            print("Average tweets per day: " + "%.2f" %
                  (float(no_of_tweets)/float(account_age_days)))
        # return tws_list
        return tws

    def prev_tweets(self, hours, minutes, user_list):
        for user in user_list:
            twlist = self.user_Tweets(user)
        # try to sort out all the tweets in tw_list as per time and then collect
        # tweets that are specified time before given time, and that are tweeted
        # by this user only


class TwitterClient(object):
    def __init__(self):
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        try:

            self.auth = OAuthHandler(consumer_key, consumer_secret)

            self.auth.set_access_token(access_token, access_token_secret)

            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")


def main():

    ap1 = TwitterClient()
    ap2 = TwitterExperiment()

    with open('result_positive.json', 'r') as f_positive:
        j_positive = json.load(f_positive)

    with open('result_negative.json', 'r') as f_negative:
        j_negative = json.load(f_negative)

    users_list = []
    timestamp_list = []
    id_list = []

    for data in j_positive:
        users_list.append(data['user'])
        id_list.append(data['id'])
        timestamp_list.append(data['timestamp'])

    for data in j_negative:
        users_list.append(data['user'])
        id_list.append(data['id'])
        timestamp_list.append(data['timestamp'])

    #print("\n len(users_list) = ", len(users_list))

    a = users_list[1:30]
    b = id_list[1:30]

    #print("\n", users_list[0:20],"\n")
    print("type of a= ", type(a), "\n type of b= ", type(b))

    # ----------------with suppress(tweepy.TweepError):----------------------------------------------------

    i = 0
    tws_list = []
    for v in users_list[0:20]:
        try:

            # time.sleep(1)
            tw_list = ap2.user_Tweets_Ids(v, id_list[i])
            i = i+1
            #print("\n ", tw_list)
            tws_list.append(tw_list)
        except tweepy.TweepError as e:
            print("\n in except block", e, v)
            continue

    # ----------------------print tw_list-------------------------------

    print("\n length of tws_list =", len(tws_list))
    # print(tws_list)
    # for tws in tws_list:
    #print("\n length of tws = ", len(tws))
    # for tw in tws:
    #   print("\n length of tw=", len(tw))

    # -------------------Main----------------------------------

    print("type of tw3", type(tw_list))
    print("\n length of tw3 list=", len(tw_list))

    for tws in tw_list:
        #print("\n type of tws = ",type(tws))

        for tw in tws:
            #print("\n type of tw = ",type(tw))

            # print("\n")
            #print("user: ",cnt_u,"tweet: ",cnt_t," ",tw[0]._json['id'])
            # print("\n",tw[0]._json['text'])
            # print("\n",tw[0]._json['created_at'])
            i = 0
            cnt_t = 0
            # ---------------Dumping to json------------------------------

            #print(json.dumps(tw._json, indent =2))

            with open('prev_tweet_json2.json', 'a') as json_data:
                json.dump(tw._json, json_data)


if __name__ == "__main__":
    main()
