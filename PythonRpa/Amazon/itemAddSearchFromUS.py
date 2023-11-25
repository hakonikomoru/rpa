# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import USSCLoginPage
from pages import ProductSearchPage
import datetime

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
loginPage = USSCLoginPage(driver, 'US')
loginPage.open()

loginPage.login('ekconnect.amazoncom.seller@gmail.com', 'hnhn8787')
productSearchPage = ProductSearchPage(loginPage.driver)
# "TSUBOE","","","","","","","","","","",""
keyWords = [
    # 知財リスト-----------------------
    # "AG Hazuki","AKER","Anello","Anker","Aputure","ARS","Astell&Kern","Audio-Technica","bandai","bandai","Beats","Beverly","Bluedio","BNISE","Boeing","Bose","Braun","BROTHER","Butterfly","Canary","Canon","Capcom","Cat Eye","CatEye","CHORD","Chroma","Chroma","Citizen","Colorata","Copic","DAIICHISEIKO","DeLonghi","Denon","Disney","Engineers","ENSKY","EPSON","Eschenbach","EZON","FEATHER","former LaQ USA","Fotopro","FUJIFILM","GLOBAL","Good Smile","Guzzini","Hammond","HARAC","Hasegawa Cutlery","havit","Hazuki","Helinox","Hobonichi","Holbein","Home star","HUAWEI","Ideaco","Intel","JapanBargain US","JBL","Jico","Kaiyodo","KAKURI","Kao","katia","katia beni","kokubo","Kokuyo","Konus","KORG","Kotobukiya","Kuretake","kyocera","Legacy","LEIFHEIT","LG","Logitech","LYNN RAMOS","Marmo printing","Marvel","MASAMOTO",
    # "MaxFactory","Max Factory","Maxon","Medicos","Megahouse","mercedes","Minosharp","Mugig","Muji","Mxson","Nikon","Nintendo","NIXON","Noppoo","OLFA","Olympus","Omron","OneTigris","Orange","Panasonic","Panasonic","Pelican","Philips","PHILIPS","Plemo","Razer","RECMOUNTS","Roland","Sanrio","Schlagwerk","Schleich","SENNHEISER","SHURE","SIDARDOE","SIGMA","Silky","SILKY","SOL REPUBLIC","Sony","Staub","SteelSeries","Sun Joe","Sun-Star Stationery","Sunstar","SUREFIRE","suzuki","SUZUKI MUSIC","Takara Tomy","TASCAM","Thunderbolt","Tojiro","Tombow","TOTO","Vess","Western Digital","XVive","ZOOM","ZWILLING J.A",
    # "1 Body","Ahava","Aidance Skincare (ie Terrasil, Femmesil)","Amope","ANSR","Avon","Baire Bottles","Balm Cosmetics","Bare Essentials cosmetics","Benefiber","Billy Jealousy","Blinc","Bliss","Borghese","Biolage","Bump","Burberry","Burt’s Bees","Butter London","Buxom Buxom","Crabtree & Evelyn","Cane + Austin","Cargo","Caudalie","Chanel","CHI","Clairsonic","Claritin","Comtrex","Crest","Cult Cosmetics","DDF","Deborah Lippmann","Dolce & Gabbana","Dr Brandt","Dr Denese","Dr Dennis Gross Skin Care","Dr Tobia","Escada","Essie","Excedrin Sinus Headache","Eyeko","Georgio Armani","Gianna Rose Atelelier","Gillette","Goldfaden MD","Godefroy Eyebrow Tint","Gucci","InStyler – many knock-offs of these were sold through Amazon.","It Works!","Jack Black","Jane Iredale","Japonesque","Jo Malone","Jouer","Juice Beauty","Juicy Couture","Julep","Kiehl’s","Korres","L’ Occitane","La Bella Donna","Lancome","Lorac","LVX","MAC cosmetics","Mario Badescu","Martrix Biolage","Mary Kay","Marvis","MDSolarSciences","Menaji Cosmetics","Michelle Phan","Molton Brown","Mustela","Nars","Nature’s Sunshine","Neutrogena","Nia 24","Norelco","Now Foods","NuBrilliance Skin Care & Skin Care Systems","Nuxe","Optimum Nutrition","Oral B","Oribe","Orlane","Oscar Blandi","Patchology","Perfume samples","Perfume testers","Perricone","Peter Thomas Roth","Philips Sonicare E-Series toothbrushes and replacement heads","Phyto","Proactive","Ralph Lauren perfume","Rodial","Sachajuan","Sara Happ","Sensa","Sheer Strength Labs","Siltra","SK II","Skyn Iceland","Somme Institute","St. Tropez","Stila","StriVectin","T3","The Art of Shaving","Theraflu Caplets","Theraflu Express Max Nighttime","Tinosorb","Urban Decay","Vimerson Health","Vincent Longo","Walkfit Platinum Orthotics","Wedderspoon Honey","Wen by Chaz Dean","Younique","Zirh","Apple","Audio-Technica","“Beats” by Dre","Bose","Brookstone","Canon Cameras - used only","Franklin Electronic","Hp","Lg","Lifeproof Phone cases","Logitech","Marantz","Microsoft","Monster Audio headphones","Native Union","Neewer","Nikon Cameras - used only","Ninja Blenders (Shark Ninja)","Otter Box","Solio","Sony Cameras - used only",
    # "Speck iPad","iPhone cases","Spigen","T-Mobile Prepaid Phones","T3","Adobe software","Beach Body","P-90X","Disney DVD","HBO","Microsoft","Rosetta Stone Language","Showtime","Sony","Warner Brothers","Dunkin Donuts","Gerber","Wedderspoon Organic Honey","Williams-Sonoma","Delta Children","ERGObaby","Evenflo","Infantimo","Munchkin","Safety First (Baby Products)","Skip Hop","Summer Infant","Unique","Cloud B","Cloudpets","Colorama","Crayola","Discovery Kids - not all, just double check","Disney","Fisher Price","Funko","Furby Connect","Frozen","Gund","Hasbro","Hot Wheels","Leapfrog","Lego","Lil Woodzeez","Little Tikes","Magformers","Mattel","Minecraft","Melissa & Doug","Moddan","Nerf","Paw Patrol","Pokemon","Skip Hop","Snoopy Sno Cone Machine","Star Wars The Force Awakens","Transformers","V-Tech","Zoomworks Stuffies","Burberry","Calvin Klein","Chico","Coach","Dickies","Dockers","Ferragamo","Icebreaker","Kate Spade","Levi’s","Michael Kors","New Balance Shoes","Nike","North Face","Playtex","Polo Ralph Lauren","RayBan","Tommy Hilfiger","Tory Burch","True Religion Brand Jeans","Uggs","Under Armour","Victoria Secret","Adidas","Adidas Originals","Brightz, Ltd","Citizen","Diesel","DKNY","Fossil","Marc by Marc Jacobs","Michele","Skagen","Amco","Big Mouth Mugs","Black & Decker","Bogzon","Breville","Calphalon","Char-Broil","Cuisinart","Cupture","Farberware","Fred & Friends","Hamilton Beach","Joseph Joseph","Kitchen Aid","Le Creuset",
    # "LED Lenser","Ledlenser","Lodge","New Metro Design","Norpro","Oxo Good Grips","Palais Glassware","Proctor Silex","Roommates","Rtic","simplehuman","Weber","Wilton","Yumco","Adidas","Asics","Clarks Shoes","Converse Shoes","Crocs","Keen","Nike","Puma","Skechers","Sperry","Toms Shoes","Uggs","Alex And Ani","American Tourister","Petsafe","Wahl",
    # favoriteリスト------------------
    # "Playstation Vita","Playstation 3","Playstation 4","Kalita","BEHRINGER","furyu","Slim Walk","Taito",
    # "Showa Note","Pilot pen","BANDAI","sony","Okada Hardware",
    # "HORI Nintendo",
    "FOTS","Hobby JAPAN","MEISTER JAPAN","Hnafuda Flower Cards","Kaiyodo","Digital Monster","Final Fantasy","Fujiya"
    # "Tamiya"
    # , "DAISO"
    # "ZEROJAPAN","ANVISH","Uni Posca","Pilot Frixion","Marcato","Pentel","Shinwa","Nanoblocks","Uni-ball","Platinum pen",
    # "Uzaki Nissin","Gel pen","Samior","ELECOM","Dragonfly pen","Shop kit Japanese series",
    # "Zebra","VESSEL""Midori MD Notebook",
    # "Asvel","STALOGY","OneOdio","Kokuyo Campus","Senkichi","Chosera","King Grit Waterstone","Meruperu",
    # "Mikisyo","Sori Yanagi","Mizu","SEGA miku","Re: Zero Rem","bandai hobby","japan import pen","Tomica",
    # "Nendoroid","kotobukiya","persona","japan import","Yoshikawa","THERMOS",
    # "OLYMPUS","Hoppetta","Coleman","japan import Puzzle","ensky","Sunstar",
    # "HORI Controller","godzilla","Itazura","hario","HORI コントローラー 有線",
    # "HORI コントローラー","コントローラー 有線",
    # "Tenyo","Tombo","TC Electronic",
    # "Chikamasa","ConsoleTuner","Ibanez","BOSS","XYZprinting","Max Factory","EVERNEW","Tamron","Electro-Harmonix",
    # "ARTISAN","TSUBOE","Square enix"
]
searchTimeLog = []
for keyWord in keyWords:
    productSearchPage.open_product_registration_page_by_url('US')
    productSearchPage.search_with_keyword(keyWord)
    dt_now = datetime.datetime.now()
    startDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    asins = productSearchPage.extract_asin_from_product('US')
    # /Users/ken.ebata/Dropbox/sellBuy/outPutFile/US
    productSearchPage.write_output_to_file('/Users/ken.ebata/Dropbox/sellBuy/outPutFile/US/asinFor'+str(
        keyWord)+str(dt_now.strftime('%Y-%m-%d %H:%M'))+'.csv', asins)

    dt_now = datetime.datetime.now()
    endDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
    log = startDateTime+"~"+endDateTime
    searchTimeLog.append(keyWord+"："+log)
    print(keyWord+"："+log)
print(searchTimeLog)

# productSearchPage.close()
# myAuctionPage.evaluate_button_press()

# アップツールも自動化視野
# https://apptool.jp/mypage
# もし確認するボタンがあった場合、前の画面に戻って次のループ
#　↑出ない場合は、評価を行う
