# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import TwitterLoginPage
from pages import TwitterPage
import chromedriver_binary
from selenium.webdriver.common.keys import Keys

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
twitterLoginPage = TwitterLoginPage(driver)
twitterPage = TwitterPage(driver)
twitterLoginPage.open()
twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
twitterPage.フォロワーリストを開く('premier_teru')
for n in range(10):
    twitterPage.非相互フォロワーをフォロー解除する(20)
    driver.get(
        'https://twitter.com/premier_teru/following'
    )
twitterPage.close()