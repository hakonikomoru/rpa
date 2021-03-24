# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import MyAmazonPage
from pages import TwitterLoginPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# twitterLoginPage = TwitterLoginPage(driver)
# twitterLoginPage.open()
# twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = MyAmazonPage(driver)
amazonPage.open()
amazonPage.対象縦長ページの商品を投稿する('https://www.amazon.co.jp/s?i=merchant-items&me=AO3JD7ELZ9RTY&page=')
amazonPage.close()
