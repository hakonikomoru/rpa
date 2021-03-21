# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
from BasePage import BasePage
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
        url = "https://www.amazon.co.jp/s?me=AO3JD7ELZ9RTY&marketplaceID=A1VC38T7YXB528"
        super().__init__(driver=driver, url=url)

    def 商品一覧からClassNamedでDOMをとる(self, className):
        return self.driver.find_elements_by_class_name(className)

    def 商品画面をURLで直接開く(self, url):
        self.driver.get(url)

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
