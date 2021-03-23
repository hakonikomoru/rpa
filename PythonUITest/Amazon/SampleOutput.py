# -*- coding: utf-8 -*-
import requests
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc import Client, WordPressPost
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import AmazonTimeSalePage
from pages import TwitterLoginPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# twitterLoginPage = TwitterLoginPage(driver)
# twitterLoginPage.open()
# twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = AmazonTimeSalePage(driver)
# amazonPage.open()

amazonPage.fileを出力(
    '/Users/ken.ebata/work/rpa/PythonUITest/outPutFile/urls.csv', ['あ','い'])
    

amazonPage.fileに追記(
    '/Users/ken.ebata/work/rpa/PythonUITest/outPutFile/urls.csv', ['う','え'])


amazonPage.close()


