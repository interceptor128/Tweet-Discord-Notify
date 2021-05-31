import requests
import json
import tweepy
import os

# 認証に必要なキーとトークン
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# 検索ワード
SearchWord = os.environ['SEARCH_WORD']

# 取得件数
CountNumber = int(os.environ['COUNT_NUMBER'])

# キーワードからツイートを取得
api = tweepy.API(auth)
tweets = api.search(q=[SearchWord], count=CountNumber,)

webhook_url = os.environ['WEBHOOK_URL']

for tweet in tweets:
    post_date = str(tweet.created_at)
    post_link = 'https://twitter.com/' + \
        tweet.user.screen_name + '/status/' + str(tweet.id)
    post_content = post_date + '\n' + post_link
    main_content = {'content': post_content}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        webhook_url, json.dumps(main_content), headers=headers)
