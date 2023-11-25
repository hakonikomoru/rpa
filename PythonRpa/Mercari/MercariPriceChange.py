# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from MercariLogin import MercariLogin


class MercariPriceUpChange:

    mercariLogin = MercariLogin()

    def execute(self):

        mercari = self.mercariLogin.getMercariLoginPage()
        ret = self.allItemPrice1YenUp(mercari)
        self.allItemPrice1YenDown(ret)
        exit

    def allItemPrice1YenUp(self, mercari):

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
            chrome.find_element_by_link_text("商品の編集").click()
            inputDefault = chrome.find_elements_by_class_name("input-default")
            sleep(1.5)
            itemName = inputDefault[0].get_attribute("value")
            inputPrice = inputDefault[1]
            sleep(1)
            try:
                defaultPrice = int(inputPrice.get_attribute("value"))
            except:
                throughCount += 1
                print(str(throughCount)+"件スルー")
                chrome.close()
                chrome.switch_to.window(handleArray[0])
                continue

            nextPrice = defaultPrice + 1
            inputDefault[1].clear()
            inputPrice.send_keys(nextPrice)
            sleep(1)
            chrome.find_element_by_xpath(xpath).click()
            print("「"+itemName+"」　価格変更完了")
            chrome.close()
            chrome.switch_to.window(handleArray[0])

        return chrome

    def allItemPrice1YenDown(self, mercari):

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
            chrome.find_element_by_link_text("商品の編集").click()
            inputDefault = chrome.find_elements_by_class_name("input-default")
            sleep(1.5)
            itemName = inputDefault[0].get_attribute("value")
            inputPrice = inputDefault[1]
            sleep(1)
            try:
                defaultPrice = int(inputPrice.get_attribute("value"))
            except:
                throughCount += 1
                print(str(throughCount)+"件スルー")
                chrome.close()
                chrome.switch_to.window(handleArray[0])
                continue

            nextPrice = defaultPrice - 1
            inputDefault[1].clear()
            inputPrice.send_keys(nextPrice)
            sleep(1)
            chrome.find_element_by_xpath(xpath).click()
            print("「"+itemName+"」　価格変更完了")
            chrome.close()
            chrome.switch_to.window(handleArray[0])

        chrome.close()


# 起動
MercariPriceUpChange().execute()

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
