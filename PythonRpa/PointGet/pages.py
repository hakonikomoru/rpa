# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import datetime

# login画面操作


class RakutenENaviLoginPage(BasePage):

    def __init__(self, driver):
        url = "https://www.rakuten-card.co.jp/e-navi/members/point/click-point/index.xhtml?l-id=enavi_mtop_pointservice_click"
        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('u')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('p')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)

# クリックでポイント


class ClickDePointPage(BasePage):

    クリックしてポイント画面DOMselector = "#contentsArea > div.contentBox02.click-point"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def aタグをすべてクリック(self):
        count = self.driver.find_element_by_id("procurablePoint").text
        curUrlFirst = self.driver.current_url
        for n in range(int(count)):
            if n == 0 or n % 2 == 0:
                continue
            dom = self.driver.find_element_by_css_selector(
                self.クリックしてポイント画面DOMselector)
            firstATag = dom.find_elements_by_tag_name("a")[int(n)]
            firstATag.click()
            sleep(5)
            handleArray = self.driver.window_handles
            self.driver.switch_to.window(handleArray[1])
            self.driver.close()
            self.driver.switch_to.window(handleArray[0])
            self.driver.get(curUrlFirst)
