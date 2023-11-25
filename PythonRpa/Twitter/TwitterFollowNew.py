# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import TwitterLoginPage
from pages import TwitterPage
import tweepy

CONSUMER_KEY = 'C1WqvprBuQpN2ibliUqc2m1F5'
CONSUMER_SECRET = 'iIf3MrbhkdChqR1ccDOr9cVmkzsDHsJLRtjAq6Z6nhg2ECl9HY'
ACCESS_TOKEN = '1553783508736573440'
ACCESS_SECRET = 'MomINNi5IRHCl4zznNA8cAL6RTFWED78i9bDIqMRW9tV0'

# twitter認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 検索キーワードと件数
q = "相互フォロー"
count = 100

# 検索実行
search_results = api.search(q=q, count=count)

for result in search_results:
    # 検索キー
    user_key = result.id
   
    username = result.user.name
    # ＠以降の内容
    user_id = result.user._json['screen_name']
    # ツイートの日時を取得
    time = result.created_at
    
    try:
        #いいね
        api.create_favorite(user_key)
        #フォロー
        api.create_friendship(user_id)
    except Exception as e:
        # すでに「いいね」、フォロー済みだとこれが出力
        print('　【失敗】' + str(e))