# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage


class USSCLoginPage(BasePage):
    
    def __init__(self, driver, land):
        if 'US' in land:
            url = "https://sellercentral.amazon.com/"
        elif 'JP' in land:
            url = 'https://sellercentral.amazon.co.jp/'

        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        self.driver.find_element_by_link_text('login').click()
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('email')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        print("40秒以内にワンタイムパスワードの入力を終えてください。")
        sleep(40)
        print("入力時間終了")
        print("login!!!")
