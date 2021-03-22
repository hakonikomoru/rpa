# coding:utf-8
import requests
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
from BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link text'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'
import os


class WordPressLoginPage(BasePage):
    def __init__(self, driver):
        url = "https://wordprees.com/ja"
        super().__init__(driver=driver, url=url)

    def ログイン(self, userName, passWord):
        self.driver.find_element_by_link_text("ログイン").click()
        sleep(5)
        search = self.driver.find_element_by_id("usernameOrEmail")
        search.send_keys(userName)
        search.send_keys(Keys.ENTER)
        sleep(5)
        search = self.driver.find_element_by_id("password")
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        sleep(5)
        for n in range(10):
            try:
                nanika = self.driver.find_element_by_link_text("プレってる")
                search = self.driver.find_element_by_id("usernameOrEmail")
                search.send_keys(userName)
                search.send_keys(Keys.ENTER)
                sleep(5)
                search = self.driver.find_element_by_id("password")
                search.send_keys(passWord)
                search.send_keys(Keys.ENTER)
            except:
                break

    def 投稿を開く(self):
        self.driver.get("https://wordpress.com/post/premieritem.wordpress.com")

    def 投稿する(self):
        # 表示されるまで待機
        sleep(15)
        self.driver.find_element_by_id(
            "post-title-0").send_keys("投稿テスト")
        # self.driver.execute_script(
        #     "document.getElementsByClassName('editor-post-title__input')[0].value = '投稿テスト';")
        # search = self.driver.execute_script(
        #     "document.getElementById('post-title-0')")
        # print(nanika)
        # self.driver.find_element_by_tag_name("textarea").send_keys("投稿テスト")
        # search =
        # self.driver.find_element_by_class_name(
        #     "editor-post-title__input").send_keys("投稿テスト")
        # search.send_keys("投稿テスト")
        # print(search)
        # self.driver.execute_script(
        #     "document.getElementById('block-082e0522-6f0c-4ce1-bba9-41d3d06f85de').innerHTML = '投稿テスト'")
        # search = self.driver.find_element_by_id(
        #     "block-082e0522-6f0c-4ce1-bba9-41d3d06f85de")
        # search.send_keys("なにか")

    def 短縮URLを返す(longUrl):
        url = 'https://api-ssl.bitly.com/v3/shorten'
        access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
        query = {
            'access_token': access_token,
            'longurl': longUrl
        }
        r = requests.get(url, params=query).json()['data']['url']
        return r
