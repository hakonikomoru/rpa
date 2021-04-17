# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
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

searchKeyword = "相互フォロー"
# もうちょっとフォロワー増やしたら、アウトバウンドで他検索でフォローし始める
# searchKeyword = "せどり"
# searchKeyword = "転売"
# searchKeyword = "メルカリ転売"
searchLimit = 100

# 検索実行
# TODO あとで検索結果のユーザーをリストアップする
# 検索結果を出力
for n in range(23):
    limit = 0
    try:
        search_results = api.search(q=searchKeyword, count=searchLimit, lang="ja")
    except:
        print("予期せぬerrorです。念の為、ブラウザでTwitterを確認してください")
        break

    for result in search_results:
        # if limit > 41:
        #     break
        if limit == 6:
            limit = 0
            print("30分休憩します。")
            sleep(1800)
            
        screen_name = result.user._json['screen_name']
        user_id = result.id
        try:
            # print(screen_name)
            # print(user_id)
            # print(result.user.following)
            # フォローしていない場合
            if result.user.following == 0:
                api.create_friendship(screen_name)
                print("「@"+screen_name+"」さんをフォローしました。")
                limit = limit + 1
                # 60*60/41 = 87.****
                # 1時間の以内に41フォローしたいので上の計算になる
                # sleep(88)
        except Exception as e:
            print(e)
            # [{'code': 161, 'message': "You are unable to follow more people at this time. Learn more <a href='http://support.twitter.com/articles/66885-i-can-t-follow-people-follow-limits'>here</a>."}]
            if "You are unable to follow more people at this time. Learn more" in str(e):
                print("怒られたので1時間休憩します。")
                sleep(3600)
                # print("怒られたので10分間休憩します。")
                # sleep(600)
                continue

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
    dt_now = datetime.datetime.now()
    print("時間終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    twitterPage.close()

    # id = input("TwitterIDを入力してください：")
    # pw = input("TwitterPWを入力してください：")
    # twitterLoginPage.Twitterログイン(id, pw)