# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
import chromedriver_binary


class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def fileを出力(self, path, outPutArr):
        # pathのファイルへ書き込む
        with open(path, mode='w') as f:
            for text in outPutArr:
                f.write(str(text)+"\n")

    def 配列内の重複を無くして配列を返す(self,arr):
        return list(set(arr))
        