# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage


class TwitterLoginPage(BasePage):
    def __init__(self, driver):
        url = "https://twitter.com/login"
        super().__init__(driver=driver, url=url)

    def Twitterlogin(self):
        sleep(5)
        search = self.driver.find_element_by_name("session[username_or_email]")
        search.send_keys("premier_teru")
        search = self.driver.find_element_by_name("session[password]")
        search.send_keys("hnhn8787")
        search.send_keys(Keys.ENTER)
