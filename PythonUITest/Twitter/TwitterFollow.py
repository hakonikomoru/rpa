# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import TwitterLoginPage
from pages import TwitterPage
import chromedriver_binary
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

# options = Options()
# options.add_argument('--headless')
# # driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
twitterLoginPage = TwitterLoginPage(driver)
twitterPage = TwitterPage(driver)
twitterLoginPage.open()
sleep(3)
targets = ['相互フォロー']
twitterLoginPage.Twitterログイン("ken_channel_nel", "hnhn8787")
twitterPage.プレってるフォローリスト()
twitterPage.表示されたユーザーリストをフォローする()
twitterPage.close()

# id = input("TwitterIDを入力してください：")
# pw = input("TwitterPWを入力してください：")
# twitterLoginPage.Twitterログイン(id, pw)

sleep(3600)
searchKeyword = "相互フォロー"
searchLimit = 100
# 検索実行
search_results = api.search(q=searchKeyword, count=searchLimit, lang="ja")
# TODO あとで検索結果のユーザーをリストアップする
# 検索結果を出力
limit = 0
for result in search_results:
    if limit > 41:
        break
    screen_name = result.user._json['screen_name']
    user_id = result.id
    try:
        print(screen_name)
        print(user_id)
        print(result.user.following)
        if result.user.following == 0:
            api.create_friendship(screen_name)
            print("「@"+screen_name+"」さんをフォローしました。")
            limit = limit + 1
    except Exception as e:
        print(e)