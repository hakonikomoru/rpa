# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import TwitterLoginPage
from pages import TwitterPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# id = input("TwitterIDを入力してください：")
# pw = input("TwitterPWを入力してください：")
driver = webdriver.Chrome()
twitterLoginPage = TwitterLoginPage(driver)
twitterPage = TwitterPage(driver)
twitterLoginPage.open()
sleep(3)
# twitterLoginPage.Twitterログイン(id, pw)
# sleep(3)
twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
targets = ['フォロバ','相互フォロー']
for target in targets:
    twitterPage.フォローアカウントリストを開く(target)
    twitterPage.表示されたユーザーリストをフォローする()

twitterLoginPage.Twitterログイン("ken_channel_nel", "hnhn8787")
for target in targets:
    twitterPage.フォローアカウントリストを開く(target)
    twitterPage.表示されたユーザーリストをフォローする()
    
twitterPage.close()
