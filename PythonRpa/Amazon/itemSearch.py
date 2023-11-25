# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import AmazonPage
from pages import ProductSearchPage

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
amazonPage = AmazonPage(driver)
amazonPage.open()
# amazonPage.search_product("BANDAI")
outPutArr = amazonPage.parse_tags_and_return_extracted_list(
    amazonPage.get_class_named_elements_from_product_page('sg-col-inner'))
amazonPage.write_output_to_file(
    '/Users/ebata/UITest/PythonRpa/outPutFile/test.csv', outPutArr)
# amazonPage.close()
