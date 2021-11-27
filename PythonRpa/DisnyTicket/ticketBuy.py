# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import DisnyTicketBuyPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
disnyTicketBuyPage = DisnyTicketBuyPage(driver)
disnyTicketBuyPage.open()
sleep(10)
disnyTicketBuyPage.購入手続きに進むボタンを押下する()
