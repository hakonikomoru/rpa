# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import GoogleAccountCreatePage
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
googleAccountCreatePage = GoogleAccountCreatePage(driver)
googleAccountCreatePage.open()
googleAccountCreatePage.名前アドレスパスワード入力(
    "江端",
    "1",
    "syokkotanTest1",
    "kensyo01",
    "kensyo01"
)
googleAccountCreatePage.電話番号を入力(
    "08067371205"
)
# # twitterLoginPage.Twitterログイン("premier_teru", "kenyuka128")
# twitterPage.フォロワーリストを開く('premier_teru')
# for n in range(10):
#     twitterPage.非相互フォロワーをフォロー解除する(20)
#     driver.get(
#         'https://twitter.com/premier_teru/following'
#     )
sleep(100)
googleAccountCreatePage.close()
