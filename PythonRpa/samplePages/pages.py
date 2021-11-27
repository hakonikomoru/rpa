# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
import chromedriver_binary


class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()


class SearchPage(BasePage):

    def __init__(self, driver):
        url = 'https://www.google.com/'
        super().__init__(driver=driver, url=url)

    def search(self, keyword):
        search_box = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search_box.send_keys(keyword + Keys.ENTER)


class ResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_result_stats(self):
        result_stats = self.driver.find_element_by_xpath('//*[@id="result-stats"]').text
        return result_stats