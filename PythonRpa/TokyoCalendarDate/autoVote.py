# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from actions import LoginPage
from webdriver_manager.chrome import ChromeDriverManager

# ヘッドレスモードオンにする場合
options = Options()
options.add_argument('--headless')
mobile_emulation = {'deviceName': 'Nest Hub'}
options.add_experimental_option('mobileEmulation', mobile_emulation)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

loginPage = LoginPage(driver)
loginPage.open()
loginPage.login('syokkotan@gmail.com', 'hnhn8787!')
loginPage.open_membership_screening_page()

vote_count = 0
for num in range(1000):
    main_content = loginPage.idで取得('mainContent')
    try:
        if num % 10 == 0:
            ng = main_content.find_element_by_id('voteNG')
            ng.click()
            print(f"{num+1}: NG")
        else:
            ok = main_content.find_element_by_id('voteOK')
            ok.click()
            print(f"{num+1}: OK")

        vote_count += 1
        print(f"{vote_count} point")
        time.sleep(2)
    except Exception as e:
        print("ボタンが無いためスキップしました。")
        print("30分経過休憩します🍵...")
        time.sleep(1800)
        loginPage.open_list_page()
        loginPage.open_membership_screening_page()
        continue
    
    if num % 50 == 0 and num > 0:
        driver.refresh()

driver.close()
