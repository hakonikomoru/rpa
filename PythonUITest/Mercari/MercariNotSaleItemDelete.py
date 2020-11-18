# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from MercariLogin import MercariLogin

class MercariNotSaleItemDelete:

    mercariLogin = MercariLogin()

    def execute(self):
        mercari = self.mercariLogin.getMercariLoginPage()
        self.notSaleItemDelete(mercari)

    def notSaleItemDelete(self, mercari):

        chrome = mercari

        pageItemMaxCount = 50
        chrome.get("https://www.mercari.com/jp/mypage/listings/listing/")
        itemAtagLists = chrome.find_elements_by_class_name("mypage-item-link")

        xpath = "/html/body/div[@class='single-container']/main[@class='single-main']/section[@class='l-single-container buy-item-container']/div[@id='sell-container']/div/div[@class='sell-container-inner']/form[@class='sell-form'][2]/div[@class='sell-content sell-btn-box']/button[@class='btn-default btn-red']"
        throughCount = 0
        for itemAtagList in itemAtagLists:
            url = itemAtagList.get_attribute("href")
            chrome.execute_script('window.open()')
            handleArray = chrome.window_handles
            chrome.switch_to.window(handleArray[1])
            chrome.get(url)
            changeBox = chrome.find_element_by_class_name("listing-item-change-box")
            redform = changeBox.find_element_by_tag_name("form")
            btnRed = redform.find_element_by_tag_name("button").text
            if btnRed == "出品を一旦停止する":
                print("削除しない")
                chrome.close()
                chrome.switch_to.window(handleArray[0])
                continue
            else:
                print("削除実行")

            actions = ActionChains(chrome)
            actions.move_to_element(changeBox)
            actions.perform()
            btnGray = changeBox.find_elements_by_tag_name("button")[1]
            btnGray.click()
            sleep(1)
            lContent = chrome.find_element_by_class_name("l-content")
            clearfix = lContent.find_element_by_class_name("clearfix")
            form = clearfix.find_element_by_tag_name("form")
            print(form)
            sleep(1)
            btn = clearfix.find_element_by_tag_name("button").click()
            print(btn)
            # lContent.find_element_by_class_name("modal-btn modal-btn-submit").click()
            sleep(2)
            chrome.close()
            chrome.switch_to.window(handleArray[0])
            continue

        chrome.close()
        exit

# 起動
MercariNotSaleItemDelete().execute()

# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
