# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
from pages import TwitterLoginPage
from pages import TwitterPage
import tweepy

for n in range(100):
    # print("1時間休憩🍵します。")
    # sleep(3600)
    options = Options()
    # options.add_argument('--headless')
    mobile_emulation = {'deviceName': 'Nest Hub'}
    # options.add_experimental_option('mobileEmulation', mobile_emulation)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    twitterLoginPage = TwitterLoginPage(driver)
    twitterPage = TwitterPage(driver)
    twitterLoginPage.open()
    sleep(3)
    targets = ['相互フォロー']
    twitterLoginPage.Twitterlogin("ken_channel_nel", "kenyuka128")
    # twitterLoginPage.Twitterlogin("ken_channel_nel", "hnhn8787")
    twitterPage.けんちゃんねるのフォロワーリスト()
    twitterPage.表示されたユーザーリストをフォローする()
    dt_now = datetime.datetime.now()
    print("時間終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    twitterPage.close()
    print("1時間休憩🍵します。")
    sleep(3600)

# id = input("TwitterIDを入力してください：")
# pw = input("TwitterPWを入力してください：")
# twitterLoginPage.Twitterlogin(id, pw)