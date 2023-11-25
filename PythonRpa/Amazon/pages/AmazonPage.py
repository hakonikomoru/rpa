from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage


class AmazonPage(BasePage):

    def __init__(self, driver):
        url = "https://www.amazon.co.jp/s?k=BANDAI&pct-off=-0&sort=-salesrank&s=date-asc-rank&high-price=10000"
        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        self.driver.find_element_by_link_text('login').click()
        search = self.driver.find_element_by_name('email')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        sleep(40)
        print("login!!!")

    def search_and_get_elements_by_class_name(self, searchWord, className):
        search_box_selector = "field-keywords"
        search_box = self.driver.find_element_by_name(search_box_selector)
        search_box.send_keys(searchWord)
        search_box.send_keys(Keys.ENTER)
        sleep(2)
        elements = self.driver.find_elements_by_class_name(className)
        return elements

    def parse_tags_and_return_extracted_list(self, elements):
        outPut = []
        for element in elements:
            div_tags = element.find_elements_by_tag_name("div")
            for div_tag in div_tags:
                data_asins = div_tag.get_attribute("data-asin")
                if data_asins is not None and len(data_asins) != 0:
                    outPut.append(data_asins)
        print(outPut)
        return outPut
