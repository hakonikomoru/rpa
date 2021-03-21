# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import MyAmazonPage
from pages import TwitterLoginPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
twitterLoginPage = TwitterLoginPage(driver)
twitterLoginPage.open()
twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = MyAmazonPage(driver)
amazonPage.open()

for num in range(15):
    amazonPage.商品画面をURLで直接開く(
        'https://www.amazon.co.jp/s?i=merchant-items&me=AO3JD7ELZ9RTY&page='+str(num+1))
    itemsTags = amazonPage.商品一覧からClassNamedでDOMをとる("a-link-normal")
    asins = []
    for itemsTag in itemsTags:
        try:
            if "/dp/" in itemsTag.get_attribute("href"):
                # ASINだけを抜く
                asins.append(itemsTag.get_attribute(
                    "href").split('/dp/')[1].split('/')[0])
        except:
            continue

    print(set(asins))
    skips = [
        # 'B079M8WTH6', 'B08JYXH1F5', 'B08PT58FS3', 'B01N12Y2FC', 'B06XCSVH7W', 'B00ZOMOJRE', 'B08XYT78VR', 'B07W33QMM4', 'B08TFH24TG', '4798623385', 'B08KWGZGD4', 'B07NDNZ9JN', 'B06XWVHZ8V', 'B08KD3B2TK', 'B08T6JXWMK', 'B08TL5W6C3',
        # 'B08WHXC3X8', 'B000AR2OYI', 'B08K3BHX2Z', 'B08VCKKD8W', 'B07DB6ZQSL', 'B00QEN65TM', 'B081RVNM49', 'B07Z4BY275', 'B08JYXB2JQ', 'B08SG7H4LX', 'B07TS6LMM7', 'B08JCDFXDW', 'B00ZOMOKVO', 'B0813R6JC6', 'B08SK1PSHD', 'B08TN72BW4',
        # 'B08RZ6YRB4', 'B08S2RYBL9', 'B08X147ZQD', 'B08HMQ3ZBT', 'B07SJYYXQ6', 'B08SBHDMSC', 'B08RYK64RQ', '4522438478', 'B08R6TMVRJ', 'B08T5TD6YV', 'B08TMV5M78', 'B08T6LCVTK', 'B0123ZAQJE', '4056115249', 'B08T5VKGPT', '4052051033'
    ]

    for asin in set(asins):
        if asin not in skips:
            amazonPage.商品画面をURLで直接開く('https://www.amazon.co.jp/dp/'+asin)
            amazonPage.Twitterボタンを押下()
            amazonPage.ツイートボタンを押下()

amazonPage.close()
