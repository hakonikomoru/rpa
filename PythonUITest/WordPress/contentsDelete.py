# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import WordPressLoginPage
import chromedriver_binary

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
wordPressLoginPage = WordPressLoginPage(driver)
wordPressLoginPage.open()
wordPressLoginPage.ログイン("syokkotan@gmail.com", "kenyuka128")
wordPressLoginPage.投稿一覧を開く()
wordPressLoginPage.投稿削除()
# wordPressLoginPage.ゴミ箱を開く()
# wordPressLoginPage.ゴミ箱削除()
wordPressLoginPage.close()
