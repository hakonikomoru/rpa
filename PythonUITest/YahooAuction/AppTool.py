# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import AppToolPage
from pages import MyAuctionPage
import chromedriver_binary

# 落札された商品のすべての取引評価を行う

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
appToolPage = AppToolPage(driver)
appToolPage.open()
loginPage.ログイン('e_ba_ta_8122@yahoo.co.jp','Kensyo01')
myAuctionPage = MyAuctionPage(loginPage.driver)
myAuctionPage.出品終了分画面をURLで直接開く()
myAuctionPage.評価ボタンを押下()

# アップツールも自動化視野
# https://apptool.jp/mypage
# もし確認するボタンがあった場合、前の画面に戻って次のループ
#　↑出ない場合は、評価を行う

myAuctionPage.close()