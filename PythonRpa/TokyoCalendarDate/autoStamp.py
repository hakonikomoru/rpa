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
loginPage.open_new_member_list()

for numCount in range(1, 10000):
    loginPage.scroll_to_bottom(5)
    womans = loginPage.ClassNameで複数のDOMを全て取得('radius0')

    if len(womans) < numCount:
        break

    icon = loginPage.ClassNameとkeyでDOMをとる('radius0', numCount)

    if not icon.is_displayed():
        print("ボタンが表示されていないためスキップしました。")
        continue

    try:
        print(f"{numCount}/{len(womans)}人目クリック")
        icon.click()
        sleep(3)
        print(f"{numCount}/{len(womans)}足跡完了")
        batu = loginPage.idで取得(
            'userProfile'
        ).find_element_by_class_name(
            'headerBar'
        ).find_element_by_class_name(
            'headerBarLeft'
        ).find_element_by_class_name(
            'hmenu_close'
        )
        batu.click()

    except Exception as e:
        print(e)
        print("ボタンが無いためスキップしました。")

driver.close()
exit()
