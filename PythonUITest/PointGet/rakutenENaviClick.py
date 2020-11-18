# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import RakutenENaviLoginPage
from pages import ClickDePointPage
import chromedriver_binary

# 落札された商品のすべての取引評価を行う

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
rakutenENaviLoginPage = RakutenENaviLoginPage(driver)
rakutenENaviLoginPage.open()
rakutenENaviLoginPage.ログイン('syokkotan','hnhn8787')
clickDePointPage = ClickDePointPage(rakutenENaviLoginPage.driver)
clickDePointPage.aタグをすべてクリック()

# アップツールも自動化視野
# https://apptool.jp/mypage
# もし確認するボタンがあった場合、前の画面に戻って次のループ
#　↑出ない場合は、評価を行う

# myAuctionPage.close()