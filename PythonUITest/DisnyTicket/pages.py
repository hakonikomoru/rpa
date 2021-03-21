# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
from BasePage import BasePage
import os
from selenium.webdriver.common.action_chains import ActionChains


# ログイン画面操作
class DisnyTicketBuyPage(BasePage):

    def __init__(self, driver):
        # url = "https://www.amazon.co.jp/"
        url = "https://reserve.tokyodisneyresort.jp/ticket/search/?numOfAdult=2&numOfJunior=0&numOfChild=0&selectParkDay1=02&parkTicketGroupCd=01&openTicket=&useDateFrom=20201212&parkTicketSalesForm=1&useDays=1&route=1&"
        super().__init__(driver=driver, url=url)

    def ログイン(self, loginId, passWord):
        self.driver.find_element_by_link_text('ログイン').click()
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('email')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        sleep(40)
        print("ログイン！！！")

    def 商品検索(self, searchWord):
        検索ボックスselector = "field-keywords"
        search = self.driver.find_element_by_name(検索ボックスselector)
        search.send_keys(searchWord)
        search.send_keys(Keys.ENTER)

    def 購入手続きに進むボタンを押下する(self):
        self.driver.find_element_by_css_selector(
            '#search-ticket-group > div > section > section.section-module.section-append > div > ul > li > button').click()

    def モーダルの確認したのelementを返す(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_css_selector(
            'body > div.new-ui-theme > div > div > ul > li > button'))
