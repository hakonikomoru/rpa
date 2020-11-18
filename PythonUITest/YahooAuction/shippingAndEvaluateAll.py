# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import LoginPage
from pages import MyAuctionPage
import chromedriver_binary

# 落札されたの商品の発送連絡とすべての取引評価を行う

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
loginPage = LoginPage(driver)
loginPage.open()
loginPage.ログイン('e_ba_ta_8122@yahoo.co.jp','Kensyo01')
myAuctionPage = MyAuctionPage(loginPage.driver)
myAuctionPage.出品終了分画面をURLで直接開く()
myAuctionPage.取引連絡ボタンを押下()
myAuctionPage.評価ボタンを押下()

# アップツールも自動化視野
# https://apptool.jp/mypage
# もし確認するボタンがあった場合、前の画面に戻って次のループ
#　↑出ない場合は、評価を行う

myAuctionPage.close()