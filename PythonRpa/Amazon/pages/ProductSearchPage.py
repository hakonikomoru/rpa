# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import datetime


class ProductSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.ASIN_URLS = {
            "US": "http://www.amazon.com/dp/",
            "JA": "http://www.amazon.co.jp/dp/",
        }

    def open_product_registration_page_by_url(self, land):
        self.driver.get(f"https://sellercentral.amazon.{land}/product-search?ref=xx_catadd_dnav_xx")

    def search_with_keyword(self, keyWord):
        sleep(3)
        search = self.driver.find_element_by_id('katal-id-0')
        search.send_keys(keyWord)
        search.send_keys(Keys.ENTER)

    def search_result_count_get(self):
        count = self.driver.find_element_by_css_selector(
            '#product-search-container > div.product-search > div > div.side-nav > div.main-content > div > div.results-header > div > div:nth-child(1)').text.split('件の')[0]
        return int(count) / 10

    def check_next_button_enabled(self):
        return bool(self.driver.find_element_by_css_selector(".next.copy-kat-button.secondary").get_property('disabled'))

    def click_next_button(self):
        try:
            next_button = self.driver.find_element_by_css_selector(".next.copy-kat-button.secondary")
            if not next_button.get_property('disabled'):
                next_button.click()
                sleep(3)
        except NoSuchElementException:
            print("Next button not found!")
    
