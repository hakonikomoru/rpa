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
driver = webdriver.Chrome()
twitterLoginPage = TwitterLoginPage(driver)
twitterPage = TwitterPage(driver)
twitterLoginPage.open()
twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
twitterPage.相互フォローアカウントリストを開く()
twitterPage.表示されたユーザーリストをフォローする()
twitterPage.close()
