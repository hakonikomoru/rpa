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

    def 投稿一覧を開く(self):
        self.driver.get("https://wordpress.com/posts/premieritem.wpcomstaging.com")
        sleep(1)

    def ゴミ箱を開く(self):
        self.driver.get("https://wordpress.com/posts/trashed/premieritem.wpcomstaging.com")
        sleep(1)

    def 投稿削除(self):
        # 一番下までスクロール
        for num in range(100):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(1)
        # 一番上まで戻る
        self.driver.execute_script('window.scroll(0,0)')
        sleep(5)
        for postItem in self.driver.find_elements_by_class_name("post-item"):
            # 一文字目が#の場合、削除する
            title = postItem.find_element_by_tag_name(
                "h1").find_element_by_tag_name(
                "a").get_attribute("data-e2e-title")
            if "#" in title[0] or len(title) > 140:
                print(title)
                # 消していく
                postItem.find_element_by_tag_name(
                "button").click()
                self.driver.find_element_by_class_name("popover__menu").find_elements_by_tag_name("button")[2].click()

    # こっちは改修が必要
    def ゴミ箱削除(self):
        # 一番下までスクロール
        for num in range(100):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(1)
        # 一番上まで戻る
        self.driver.execute_script('window.scroll(0,0)')
        sleep(5)
        for postItem in self.driver.find_elements_by_class_name("post-item"):
            # 一文字目が#の場合、削除する
            title = postItem.find_element_by_tag_name(
                "h1").find_element_by_tag_name(
                "a").get_attribute("data-e2e-title")
            if "#" in title[0]:
                print(title)
                # 消していく
                postItem.find_element_by_tag_name(
                "button").click()
                self.driver.find_element_by_class_name("popover__menu").find_elements_by_tag_name("button")[2].click()
