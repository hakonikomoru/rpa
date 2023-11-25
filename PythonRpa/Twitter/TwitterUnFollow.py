# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import TwitterLoginPage
from pages import TwitterPage
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
twitterLoginPage = TwitterLoginPage(driver)
twitterPage = TwitterPage(driver)
twitterLoginPage.open()
# twitterLoginPage.Twitterlogin("premier_teru", "hnhn8787")
twitterLoginPage.Twitterlogin("ken_channel_nel", "hnhn8787")
# twitterLoginPage.Twitterlogin("premier_teru", "kenyuka128")
driver.get(
    'https://twitter.com/ken_channel_nel/following'
)
for n in range(10):
    twitterPage.非相互フォローのフォロー解除する(5)
    driver.get(
        # 'https://twitter.com/premier_teru/following'
        'https://twitter.com/ken_channel_nel/following'
    )
twitterPage.close()