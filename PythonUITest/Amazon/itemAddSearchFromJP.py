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
loginPage = USSCLoginPage(driver, 'JP')
loginPage.open()

loginPage.ログイン('k.ebata.mail@gmail.com', 'hnhn8787')
productSearchPage = ProductSearchPage(loginPage.driver)
# "TSUBOE","","","","","","","","","","",""
# 待機
# "ZERO JAPAN","Marcato","","","","","","","","","",""
keyWords = [
    # 出品制限確認-----------------
    # "APPLE","BenQ Japan","BOSE","BROTHER","CANON","CAPTAIN STAG","CASIO","DJI","EPSON","ELECOM","Ergobaby",
    # "FUJIFILM","GOPRO","Hoppetta","Microsoft","OLYMPUS","PENTAX","RICOH","SIGMA","SONY","TAMRON","coleman",
    # "象印","サーモス","Beats","Casio","Fhilips","GoPro","Nikon","Panasonic","SanDisc","SENNHEISER","Shop Japan",
    # "YAMAHA","A BATHING APE","Abercrombie & Fitch","adidas","BOTTEGA VENETA","BURBERRY","CALVIN KLEIN","CANADA GOOSE",
    # "CHAN LUU","Chloe","Christian Louboutin","COACH","Daniel Wellington","Dior","Dunhill","Ed Hardy","emu","FENDI",
    # "FJALL RAVEN","Giorgio Armani","GOYARD","GUCCI","GUESSS","HUNTER","IL BISONTE","LeSportsac","LONGCHAMP","LOUIS VUITTON",
    # "MARC BY MARC JACOBS","Mila schon","MINNETONKA","MONCLER","NEW BALANCE","NIKE","Orobianco","PANERAI","Paul Smith",
    # "Polo Ralph Lauren","RAY-BAN","Salvatore Ferragamo","TATRAS","TIFFANY","TOD’S","TOMS SHOES","TORY BURCH","Vivienne Westwood",
    # "VANS","アンパンマン","ガンダムフィギュア","グッドスマイルカンパニー","ジブリ","たまごっち","トミカ","トーマス","ディズニー","プラレール","ぽぽちゃん",
    # "りかちゃん","レゴ","BANDAI","LEGO","SEGA","TAKARA TOMY",
    # 出品申請許可済み-----------------
    # "sony","SureFire","Coleman",
    # 出品自由------------------------
    # "ゲームキューブ コントローラー","ゲームキューブ","HORI コントローラー","コントローラー 有線",
    # "Playstation Vita","Playstation 3","Playstation 4","Kalita","BEHRINGER","furyu","Slim Walk","Taito",
    # "Showa Note","Tamiya","BANDAI","Okada Hardware","ZERO JAPAN","ANVISH","Uni Posca","Pilot Frixion",
    "Shinwa", "Nanoblocks", "Uzaki Nissin", "Gel pen", "Samior", "ELECOM", "VESSEL""Midori MD Notebook",
    "Asvel", "STALOGY", "OneOdio", "Kokuyo Campus", "Senkichi", "Chosera", "King Grit Waterstone", "Meruperu",
    "Mikisyo", "Sori Yanagi", "Mizu", "SEGA miku", "Re: Zero Rem", "bandai hobby", "japan import pen", "Tomica",
    "Nendoroid", "kotobukiya", "persona", "japan import", "Yoshikawa", "THERMOS", "OLYMPUS", "Hoppetta", "japan import Puzzle",
    "ensky", "Sunstar", "Tenyo", "Tombo", "TC Electronic", "Chikamasa", "ConsoleTuner", "Ibanez", "BOSS", "XYZprinting",
    "Max Factory", "EVERNEW", "Tamron", "Electro-Harmonix", "ARTISAN", "TSUBOE", "Square enix"
]
searchTimeLog = []
for keyWord in keyWords:
    productSearchPage.商品登録画面をURLで直接開く('JA')
    productSearchPage.検索キーワードを入力して検索する(keyWord)
    dt_now = datetime.datetime.now()
    startDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    asins = productSearchPage.商品のASINを抜き取る('JA')
    productSearchPage.fileを出力('/Users/ebata/Dropbox/sellBuy/outPutFile/JP/asinFor'+str(
        keyWord)+str(dt_now.strftime('%Y-%m-%d %H:%M'))+'.csv', asins)

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
