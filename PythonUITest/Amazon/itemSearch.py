# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import AmazonPage
from pages import ProductSearchPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
amazonPage = AmazonPage(driver)
amazonPage.open()
# amazonPage.商品検索("BANDAI")
outPutArr = amazonPage.DOMを回してタグを解析して抽出リストを返す(
    amazonPage.商品ページからClassNamedでDOMをとる('sg-col-inner'))
amazonPage.fileを出力(
    '/Users/ebata/UITest/PythonUITest/outPutFile/test.csv', outPutArr)
# amazonPage.close()
