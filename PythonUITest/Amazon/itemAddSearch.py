# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import USSCLoginPage
from pages import ProductSearchPage
import chromedriver_binary
import datetime

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
loginPage = USSCLoginPage(driver)
loginPage.open()

loginPage.ログイン('ekconnect.amazoncom.seller@gmail.com','hnhn8787')
productSearchPage = ProductSearchPage(loginPage.driver)
# ,"","","","","",""
keyWords = ["Kalita","BEHRINGER","furyu","Slim Walk","Taito","Showa Note","Pilot pen","Tamiya","BANDAI","sony","Okada Hardware","ZEROJAPAN","ANVISH","Uni Posca","Pilot Frixion","Marcato","Pentel","Shinwa","Nanoblocks","Uni-ball","Platinum pen","Uzaki Nissin","Gel pen","Samior","ELECOM","Dragonfly pen","Shop kit Japanese series","Zebra","VESSEL""Midori MD Notebook","Asvel","STALOGY","OneOdio","Kokuyo Campus"]
keyWords = ["Senkichi","Chosera","King Grit Waterstone","Meruperu","Mikisyo","Sori Yanagi","Mizu","SEGA miku","Re: Zero Rem","bandai hobby"]
keyWords = ["japan import pen","Tomica","Nendoroid","kotobukiya","persona",""]

searchTimeLog = []
for keyWord in keyWords:
    productSearchPage.商品登録画面をURLで直接開く()
    productSearchPage.検索キーワードを入力して検索する(keyWord)
    dt_now = datetime.datetime.now()
    startDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    asins = productSearchPage.商品のASINを抜き取る()
    productSearchPage.fileを出力('/Users/ebata/work/UITest/PythonUITest/outPutFile/asinFor'+str(keyWord)+str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))+'.csv',asins)
    dt_now = datetime.datetime.now()
    endDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    log = startDateTime+"~"+endDateTime
    searchTimeLog.append(keyWord+"："+log)
    print(keyWord+"："+log)
print(searchTimeLog)

# productSearchPage.close()
# myAuctionPage.評価ボタンを押下()

# アップツールも自動化視野
# https://apptool.jp/mypage
# もし確認するボタンがあった場合、前の画面に戻って次のループ
#　↑出ない場合は、評価を行う
