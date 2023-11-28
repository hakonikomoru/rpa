# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


class MercariLogin:

    chrome = webdriver.Chrome()
    mercari = ""

    def __init__(self):

        chrome = self.chrome

        chrome.maximize_window()
        chrome.get(
            "https://www.mercari.com/jp/login/?login_callback=https%3A%2F%2Fwww.mercari.com%2Fjp%2F")
        chrome.find_element_by_id("google-login").click()
        sleep(3)
        handleArray = chrome.window_handles
        chrome.switch_to.window(handleArray[1])
        for n in range(10):
            try:
                chrome.find_element_by_id(
                    "identifierId").send_keys("syokkotan@gmail.com")
                chrome.find_element_by_class_name("CwaK9").click()
                break
            except:
                continue
        sleep(2)
        for n in range(10):
            try:
                chrome.find_element(By.NAME, "password").send_keys("hnhn8787")
                chrome.find_element_by_class_name("CwaK9").click()
                break
            except:
                continue

        sleep(3)
        chrome.switch_to.window(handleArray[0])
        self.setMercariLoginPage(chrome)

    # loginした状態のメルカリを渡す
    def getMercariLoginPage(self):
        return self.mercari

    def setMercariLoginPage(self, chrome):
        self.mercari = chrome
        sleep(3)
