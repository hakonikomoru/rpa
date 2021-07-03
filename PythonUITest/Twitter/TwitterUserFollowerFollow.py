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

endFlg = 0
screenName = 'NoGucci110'
limit = 0
for n in range(23):
    followers_ids = tweepy.Cursor(api.followers_ids, screenName, -1).items()

    followers_ids_list = []
    try:
        for followers_id in followers_ids:
            followers_ids_list.append(followers_id)
    except tweepy.error.TweepError as e:
        print(e)
        print("予期せぬerrorです。念の為、ブラウザでTwitterを確認してください")
        break
    
    print(followers_ids_list)
    for follower in followers_ids_list:
        if limit == 5:
            limit = 0
            dt_now = datetime.datetime.now()
            print("30分休憩："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
            sleep(1800)
        
        try:
            # フォローしていない場合
            if api.get_user(follower).following == 0:
                api.create_friendship(follower)
                # print("「@"+str(follower.screen_name)+"」さんをフォローしました。")
                print("「@"+str(follower)+"」さんをフォローしました。")
                limit = limit + 1
                # 60*60/41 = 87.****
                # 1時間の以内に41フォローしたいので上の計算になる
                # sleep(88)
            else:
                print("フォロー済でした。")
        except Exception as e:
            print(e)
            # [{'code': 161, 'message': "You are unable to follow more people at this time. Learn more <a href='http://support.twitter.com/articles/66885-i-can-t-follow-people-follow-limits'>here</a>."}]
            # [{'code': 326, 'message': 'To protect our users from spam and other malicious activity, this account is temporarily locked. Please log in to https://twitter.com to unlock your account.'}]
            if "You are unable to follow more people at this time. Learn more" in str(e):
                print("怒られたので1時間休憩します。")
                sleep(3600)
                # print("怒られたので10分間休憩します。")
                # sleep(600)
                continue

            if "To protect our users from spam and other malicious activity, this account is temporarily locked. Please log in to https://twitter.com to unlock your account." in str(e):
                print("警告が来たので終了します。")
                endFlg = 1

    if endFlg == 1:
        break



    # try:
    #     followers = tweepy.Cursor(api.followers,screenName, -1).pages(n)
    #     print(followers)
    #     # followers = api.followers(screenName, -1)
    # except Exception as e:
    #     print(e)
    #     print("予期せぬerrorです。念の為、ブラウザでTwitterを確認してください")
    #     break

    # for follower in followers:
    #     if limit == 5:
    #         limit = 0
    #         print("30分休憩します。")
    #         sleep(1800)
                
    #     try:
    #         # フォローしていない場合
    #         if follower.following == 0:
    #             api.create_friendship(follower.screen_name)
    #             print("「@"+str(follower.screen_name)+"」さんをフォローしました。")
    #             limit = limit + 1
    #             # 60*60/41 = 87.****
    #             # 1時間の以内に41フォローしたいので上の計算になる
    #             # sleep(88)
    #         else:
    #             print("フォロー済でした。")
    #     except Exception as e:
    #         print(e)
    #         # [{'code': 161, 'message': "You are unable to follow more people at this time. Learn more <a href='http://support.twitter.com/articles/66885-i-can-t-follow-people-follow-limits'>here</a>."}]
    #         # [{'code': 326, 'message': 'To protect our users from spam and other malicious activity, this account is temporarily locked. Please log in to https://twitter.com to unlock your account.'}]
    #         if "You are unable to follow more people at this time. Learn more" in str(e):
    #             print("怒られたので1時間休憩します。")
    #             sleep(3600)
    #             # print("怒られたので10分間休憩します。")
    #             # sleep(600)
    #             continue

    #         if "To protect our users from spam and other malicious activity, this account is temporarily locked. Please log in to https://twitter.com to unlock your account." in str(e):
    #             print("警告が来たので終了します。")
    #             endFlg = 1

    # if endFlg == 1:
    #     break

    # print("15分半待ちます。")
    # sleep(900)
