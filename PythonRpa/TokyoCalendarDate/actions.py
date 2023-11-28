# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import os
from selenium.webdriver.common.action_chains import ActionChains


# login画面操作
class LoginPage(BasePage):

    def __init__(self, driver):
        url = "https://m.facebook.com/login.php?skip_api_login=1&api_key=1138624606153113&kid_directed_site=0&app_id=1138624606153113&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fclient_id%3D1138624606153113%26redirect_uri%3Dhttps%253A%252F%252Ftokyo-calendar-date.jp%252Ffacebook_connect%252Foauth_back%252Flogin%26scope%3Demail%252Cuser_friends%252Cuser_birthday%252Cuser_gender%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D56a9cfd8-183f-4e46-9c36-342c05d21c80%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftokyo-calendar-date.jp%2Ffacebook_connect%2Foauth_back%2Flogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=ja_JP&pl_dbl=0&refsrc=deprecated&_rdr"
        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        search = self.driver.find_element(By.NAME, 'email')
        search.send_keys(loginId)
        sleep(1)
        search = self.driver.find_element(By.NAME, 'pass')
        search.send_keys(passWord)
        sleep(1)
        search.send_keys(Keys.ENTER)
        sleep(2)
        print("login!!!")
        sleep(10)

    def ClassNameで複数のDOMを全て取得(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)

    def ClassNameで複数のDOMをとる(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)[1]

    def ClassNameとkeyでDOMをとる(self, className, num):
        return self.driver.find_elements(By.CLASS_NAME, className)[num]

    def いいねボタンを取得(self): # >いいね<がテキストのボタンが多いため一つ下のdefを使用
        return self.driver.find_element_by_link_text('いいね')

    def idで取得(self, id):
        return self.driver.find_element_by_id(id)

    def いいねボタンをクリック(self):
        self.driver.find_element_by_css_selector(
            '#user_buttons > div > a'
        ).click()

    def いいねボタンをクリックPremium(self):
        self.driver.find_element_by_css_selector(
            '#user_buttons > div > div > div:nth-child(1) > div > a'
        ).click()
        

    def ClassNameでDOMをとる(self, className):
        return self.driver.find_element_by_class_name(className)[1]

    def ClassNameで単体のDOMをとる(self, className):
        return self.driver.find_element_by_class_name(className)

    def open_list_page(self):
        self.driver.get('https://tokyo-calendar-date.jp/search/list#_=_')
        sleep(4)

    def open_new_member_list(self):
        self.driver.get('https://tokyo-calendar-date.jp/search/list/1')
        sleep(4)

    def login順一覧を開く(self):
        self.driver.get('https://tokyo-calendar-date.jp/search/list/2')
        sleep(4)

    def open_membership_screening_page(self):
        self.driver.get('https://tokyo-calendar-date.jp/vote')
        sleep(4)

    def search_product(self, searchWord):
        search_box_selector = "field-keywords"
        search = self.driver.find_element(By.NAME, search_box_selector)
        search.send_keys(searchWord)
        search.send_keys(Keys.ENTER)

    def click_proceed_to_checkout_button(self):
        self.driver.find_element_by_css_selector(
            '#search-ticket-group > div > section > section.section-module.section-append > div > ul > li > button').click()

    def モーダルの確認したのelementを返す(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_css_selector(
            'body > div.new-ui-theme > div > div > ul > li > button'))

    def scroll_to_top(self):
        self.driver.execute_script('window.scroll(0,0)')
    
    def scroll_to_bottom(self, scrollCount):
        for num in range(scrollCount):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(5)

    def 少しスクロール(self, scrollCount):
        for num in range(scrollCount):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,720)')
            sleep(2)
