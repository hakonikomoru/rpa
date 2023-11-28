# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import os
import datetime
import requests
import tweepy

class MercariShopsPage(BasePage):
    
    def __init__(self, driver):
        url = "https://jp.mercari.com/signin/email?params=client_id%3DnUYFDEaF6MNQgA5f0Xyx0xNXijNzp68u%26nonce%3DJQWcspQfv9jtipesZefA7n%26redirect_uri%3Dhttps%253A%252F%252Fmercari-shops.com%252Fauth%252Fcallback%252Fmercari%26response_type%3Dcode%26scope%3Duser%253Aprofile%253Aread%2Buser%253Aemail%253Aread%2Buser%253Aprivate_profile%253Aread%2Buser%253Amercari_user_id%253Aread%2Boffline_access%2Bopenid%2Bmercari_shops%26state%3Dsignin%253Dtrue"
        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        # self.driver.find_element_by_link_text('login').click()
        # 検索語として「selenium」と入力し、Enterキーを押す。
        sleep(5)
        search = self.driver.find_element(By.NAME, 'email')
        search.send_keys(loginId)
        sleep(2)
        search = self.driver.find_element(By.NAME, 'password')
        search.send_keys(passWord)
        sleep(2)
        search.send_keys(Keys.ENTER)
        print('login!!!')

    def get_class_named_elements_from_product_list(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)

    def get_one_dom_from_product_list_by_classname(self, className):
        return self.driver.find_element_by_class_name(className)

    def get_dom_by_selector(self, selector):
        return self.driver.find_element_by_xpath(selector)

    def get_dom_from_product_list_by_tagname(self, tagName):
        return self.driver.find_elements(By.TAG_NAME, tagName)
    
    def open_product_page_directly_by_url(self, url):
        self.driver.get(url)
        sleep(5)

    def transition_to_edit_screen(self, path):
        cur_url = self.driver.current_url
        self.driver.get(cur_url+path)
        sleep(5)
    
    def scroll_to_top(self):
        self.driver.execute_script('window.scroll(0,0)')
    
    def scroll_to_bottom(self, scrollCount):
        for num in range(scrollCount):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(2)

    def write_output_to_file(self, path, outPutArr):
        # pathのファイルへ書き込む
        with open(path, mode='w') as f:
            for text in outPutArr:
                f.write(str(text)+"\n"+"\n")

    def append_to_file(self, path, mergeArr):
        # pathのファイルへ書き込む
        with open(path, mode='a') as f:
            for text in mergeArr:
                f.write(str(text)+"\n")