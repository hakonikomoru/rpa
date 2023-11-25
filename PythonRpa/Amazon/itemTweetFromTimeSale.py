# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from BasePage import BasePage
import datetime
from pages.AmazonTimeSalePage import AmazonTimeSalePage
import tweepy
from webdriver_manager.chrome import ChromeDriverManager
import os
import config

# APIの認証
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
# Twitterオブジェクトの生成
api = tweepy.API(auth)

# options = Options()
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()

sleep(5)
urls = []

dt_now = datetime.datetime.now()
range_count = 80

amazon_page = AmazonTimeSalePage(driver)
amazon_page.open()

# Twitterトレンドを見てハッシュタグを調整しよう
amazon_page.open_product_page_directly_by_url(
    'https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fprimeday%3Fref_%3Dnav_custrec_signin%26_encoding%3DUTF8&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
)
# amazon_page.login("premier_teru", "hnhn8787")
amazon_page.login('k.ebata.mail@gmail.com', 'hnhn8787')
amazon_page.open_product_page_directly_by_url(
    'https://www.amazon.co.jp/gp/goldbox/all-deals/?ie=UTF8&ref_=sv_whd_1'
)

today = datetime.date.today().strftime("%Y-%m-%d")
file_path = f"/Users/ken.ebata/work/rpa/PythonRpa/outPutFile/asins{today}.csv"

if not os.path.exists(file_path):
    with open(file_path, mode='w') as f:
        f.write("dummy")

with open(file_path) as f:
    old_asins = f.read()

not_title_count = 0
selector_get_miss_count = 0
sou_count = 0
atag_asins = []
skip_atags_asins = []

dt_now = datetime.datetime.now()
print(f"タイムセールURL収集開始：{dt_now.strftime('%Y-%m-%d %H:%M:%S')}")

urls = amazon_page.process_range_count(
    amazon_page, range_count, skip_atags_asins
)

dt_now = datetime.datetime.now()
print("タイムセールURL収集終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))

skip_asins = []
post_count = 0
dp_in_asins = []
skip_urls = []

for url in urls:
    asins = amazon_page.collect_asins(url)
    amazon_page.process_asins(
        asins, skip_asins, skip_urls, BasePage, api, post_count, amazon_page, file_path
    )
    amazon_page.open_next_page()

amazon_page.close()
