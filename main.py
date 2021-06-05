import requests
import json
import tweepy
import os
import psycopg2
from datetime import timedelta


def twitter_api():
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api


def search_tweet():
    # Call Twitter API
    api = twitter_api()
    search_word = os.environ['SEARCH_WORD']
    count_number = int(os.environ['COUNT_NUMBER'])
    tweets = api.search(
        q=[search_word], locale='ja', result_type='mixed', count=count_number)

    return tweets


def db_connect():
    con = psycopg2.connect(os.environ['DATABASE_URL'])

    return con


def select_execute(con, sql, screen_name, tweet_id):
    with con.cursor() as cur:
        cur.execute(sql, (screen_name, tweet_id))
        rows = cur.fetchall()

    return rows


def insert_execute(con, sql, screen_name, tweet_id):
    with con.cursor() as cur:
        cur.execute(sql, (screen_name, tweet_id))

    con.commit()


def create_content(created_at, screen_name, tweet_id):
    created_at += timedelta(hours=9)
    post_date = str(created_at)
    post_link = 'https://twitter.com/' + screen_name + '/status/' + tweet_id
    post_content = post_date + '\n' + post_link

    return post_content


if __name__ == '__main__':
    print('Search Fan Art Tweet')
    tweets = search_tweet()

    webhook_url = os.environ['WEBHOOK_URL']

    print('Connect Heroku Postgres')
    con = db_connect()

    for tweet in tweets:
        print('Check Table "twitter" key=%s, %s' %
              (tweet.user.screen_name, tweet.id_str))
        sql = 'select * from twitter where screen_name = %s and tweet_id = %s'
        res = select_execute(con, sql, tweet.user.screen_name, tweet.id_str)

        # No post tweet
        if len(res) == 0:
            # Create post content
            post_content = create_content(
                tweet.created_at, tweet.user.screen_name, tweet.id_str)

            # Create header
            main_content = {'content': post_content}
            headers = {'Content-Type': 'application/json'}

            print('Post Discord Channel')
            response = requests.post(
                webhook_url, json.dumps(main_content), headers=headers)

            print('Insert Tweet of Posted content')
            sql = "INSERT INTO twitter (screen_name, tweet_id) VALUES(%s, %s);"
            insert_execute(con, sql, tweet.user.screen_name, str(tweet.id))
        else:
            print("No tweet")
