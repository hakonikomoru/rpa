# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import TwitterLoginPage
from pages import TwitterPage
import chromedriver_binary
import tweepy

for n in range(23):
    # print("1時間休憩します。")
    # sleep(3600)
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
    # twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
    twitterPage.カンのフォローリスト()
    twitterPage.表示されたユーザーリストをフォローする()
    dt_now = datetime.datetime.now()
    print("時間終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    twitterPage.close()
    print("1時間休憩します。")
    sleep(3600)

# id = input("TwitterIDを入力してください：")
# pw = input("TwitterPWを入力してください：")
# twitterLoginPage.Twitterログイン(id, pw)