# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import WordPressLoginPage
import chromedriver_binary
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import requests
import tweepy


# 認証に必要なキーとトークン
API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Twitterオブジェクトの生成
api = tweepy.API(auth)

# ツイートを投稿
try:
    api.update_status("テスト投稿")
except Exception as e:
    print(e)
    if "User is over daily status update limit" in str(e):
        print("3時間以内に300件投稿を行いました")
    elif "duplicate" in str(e):
        print("重複した投稿内容です")
    # 返ってくるやつ
    # [{'code': 185, 'message': 'User is over daily status update limit.'}]
    # [{'code': 187, 'message': 'Status is a duplicate.'}]


# キーワードからツイートを取得
# api = tweepy.API(auth)
# tweets = api.search(q=['Python'], count=10)

# for tweet in tweets:
#     print('-----------------')
#     print(tweet.text)

sleep(1000)
# 値段をとってきたい
# 画像をとってきたい


# URLを短縮する
# longUrl = "https://amazon.co.jp/gp/product/B08X5NTJSR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22&aod=1"
# url = 'https://api-ssl.bitly.com/v3/shorten'
# access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
# query = {
#     'access_token': access_token,
#     'longurl': longUrl
# }
# createUrl = requests.get(url, params=query).json()['data']['url']

wp = Client('https://premieritem.wpcomstaging.com/xmlrpc.php',
            "syokkotan", "kenyuka128")
post = WordPressPost()
title = "テスト"
post.title = title
post.content = "aaa"
# post.content = "<h2>"+createUrl+"\n#amazon</h2>"
# post.content = '<a href="https://kostrivia.com/531.html">Google</>'
# post.description = 'This is the body of my new post.'
# post.tags = 'test, firstpost'
post.terms_names = {'category': ["プレってる", "品薄商品"]}
# post.post_status = 'publish'
post.post_status = 'draft'
wp.call(NewPost(post))
# 試す
# https://qiita.com/mima_ita/items/968f22f54c3febd5360f


