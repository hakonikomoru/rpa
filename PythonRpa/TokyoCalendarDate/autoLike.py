# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
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
likeCount = 0
for num in range(3000):
    loginPage.open_list_page()
    # loginPage.open_new_member_list()
    # loginPage.login順一覧を開く()
    try:
        oneWoman = loginPage.ClassNameで複数のDOMをとる('radius0')
        print(str(num+1)+"人目クリック")
        # ここの待機時間をランダムにしたほうが良さそう
        sleep(3)
        oneWoman.click()
        sleep(3)
        loginPage.いいねボタンをクリック()
        # loginPage.いいねボタンをクリックPremium()
        likeCount += 1
        print(str(num+1)+"人目いいね完了")
    except Exception as e:
        print(e)
        print("ボタンが無いためスキップしました。")
        continue 
    
    sleep(2)

print(str(likeCount)+"人のいいねが完了しました！")
driver.close()
exit()
