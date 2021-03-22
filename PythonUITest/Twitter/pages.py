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


class TwitterLoginPage(BasePage):
    def __init__(self, driver):
        url = "https://twitter.com/login"
        super().__init__(driver=driver, url=url)

    def Twitterログイン(self, userName, passWord):
        sleep(5)
        search = self.driver.find_element_by_name("session[username_or_email]")
        search.send_keys(userName)
        search = self.driver.find_element_by_name("session[password]")
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)


class TwitterPage(BasePage):
    def __init__(self, driver):
        url = 'https://twitter.com/search?q=%E7%9B%B8%E4%BA%92%E3%83%95%E3%82%A9%E3%83%AD%E3%83%BC&src=typed_query&f=user'
        super().__init__(driver=driver, url=url)

    def 商品一覧からClassNamedでDOMをとる(self, className):
        return self.driver.find_elements_by_class_name(className)

    def 商品画面をURLで直接開く(self, url):
        self.driver.get(url)

    def 相互フォローアカウントリストを開く(self):
        self.driver.get(
            'https://twitter.com/search?q=%E7%9B%B8%E4%BA%92%E3%83%95%E3%82%A9%E3%83%AD%E3%83%BC&src=typed_query&f=user'
        )

    def 表示されたユーザーリストをフォローする(self):
        sleep(10)
        for scrollCount in range(30):
            for scrollCount in range(30):
                wait = WebDriverWait(self.driver, 20)
                # 指定された要素(検索テキストボックス)が表示状態になるまで待機する
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (By.CLASS_NAME, "css-1dbjc4n")
                    )
                )
                print(scrollCount)
                self.driver.execute_script('window.scroll(0,1000000)')
                sleep(1)

            for count in range(500):
                self.driver.execute_script('window.scroll(0,1000000)')
                spanTags = self.driver.find_elements_by_tag_name("span")
                for spanTag in spanTags:
                    try:
                        if "フォロー" == spanTag.text:
                            print(spanTag.text)
                            spanTag.click()
                            break
                    except:
                        continue

    def Twitterボタンを押下(self):
        aTags = self.driver.find_elements_by_tag_name("a")
        for aTag in aTags:
            try:
                if "Twitterでシェアする" in aTag.get_attribute("title"):
                    aTag.click()
            except:
                continue

    def ツイートボタンを押下(self):
        sleep(5)
        # タブを見るカーソルが変わっていないため、一度タブを切り替える
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(self.driver.window_handles[1])
        spanTags = self.driver.find_elements_by_tag_name("span")

        for spanTag in spanTags:
            try:
                if "ツイートする" in spanTag.text:
                    spanTag.click()
                    break
            except:
                continue

        handleArray = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handleArray[0])

    def 短縮URLを返す(longUrl):
        url = 'https://api-ssl.bitly.com/v3/shorten'
        access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
        query = {
            'access_token': access_token,
            'longurl': longUrl
        }
        r = requests.get(url, params=query).json()['data']['url']
        return r
