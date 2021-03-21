
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


class WowmaItemDelete:

    chrome = webdriver.Chrome()

    def openOneTimeDisplay(self):

        chrome = self.chrome

        # ブラウザを開く。
        chrome.get("https://sg.manager.wowma.jp/wmshopclient/authclient/login")
        # 検索語として「selenium」と入力し、Enterキーを押す。
        chrome.find_element_by_id("loginId").send_keys("dev@hunglead.com")
        chrome.find_element_by_id("password").send_keys("yxa5zv6P")
        chrome.find_element_by_id("btnLogin").click()

        oneTimePass = self.getOneTimePass()

        chrome.find_element_by_id("oneTimeKey").send_keys(oneTimePass)
        chrome.find_element_by_id("btnSearch").click()

        self.chrome = chrome

    def execute(self):

        self.openOneTimeDisplay()

        chrome = self.chrome

        # 10回とりあえずチェレンジ
        for n in range(10):
            num = n + 1
            print(str(num)+"回目のチャレンジ")
            try:
                chrome.find_element_by_id("oneTimeKey")
                print("入力したワンタイムキーが不正です。")
            except:
                print("ワンタイムキー入力成功！")
                break

            oneTimePass = self.getOneTimePass()
            # 入力した文字列を削除
            chrome.find_element_by_id("oneTimeKey").clear()
            chrome.find_element_by_id("oneTimeKey").send_keys(oneTimePass)
            chrome.find_element_by_id("btnSearch").click()

        menu1 = "商品・画像・デザイン"
        chrome.find_element_by_link_text(menu1).click()
        sleep(1)
        menu2 = "商品一覧"
        chrome.find_element_by_link_text(menu2).click()

        sleep(5)

        searchItemCode = input("削除したい商品コードを入力してください：")
        chrome.find_element_by_id("searchKwd_ctl").send_keys(searchItemCode)
        itemCodeRadioButtonXpath = '//*[@id="_search_main_frm"]/div[4]/div[2]/div/div[2]/span/label[4]'
        chrome.find_element_by_xpath(itemCodeRadioButtonXpath).click()
        chrome.find_element_by_id("btnSearch").click()
        sleep(2)
        chrome.find_element_by_link_text("200").click()

        chrome.find_element_by_class_name(
            "wm-checkbox wm-checkbox-nolabel").click()

        # 普通にエレメントを取得する
        saleStatusSelectBox = chrome.find_element_by_name('allSellStsKbnTop')
        # 取得したエレメントをSelectタグに対応したエレメントに変化させる
        saleStatusSelectBoxElement = Select(saleStatusSelectBox)
        # 選択したいvalueを指定する
        saleStatusSelectBoxElement.select_by_value("2")

        chrome.find_element_by_id("allUpDateTop").click()

        sleep(60)

        chrome.close()
        exit()

    # 　Wowma!ワンタイムキー取得

    def getOneTimePass(self):

        firefox = webdriver.Firefox()

        firefox.get("https://x8zpl.cybozu.com/login")
        # 検索語として「selenium」と入力し、Enterキーを押す。
        firefox.find_element_by_id("username-:0-text").send_keys("江端健")
        firefox.find_element_by_id("password-:1-text").send_keys("ebata1205")
        firefox.find_element_by_class_name("login-button").click()

        sleep(1)

        # サイボウズofficeボタンクリック
        serviceslashs = firefox.find_elements_by_class_name("service-slash")
        for serviceslash in serviceslashs:
            serviceslash.click()
            break

        sleep(2)
        # メールワイズクリック
        mailWiseXpath = "/html/body/div[2]/div[1]/div[3]/div[2]/span[23]/a/img"
        firefox.find_element_by_xpath(mailWiseXpath).click()
        sleep(1)
        # 開発クリック
        devXpath = "/html/body/div[2]/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr/td[3]/a"
        firefox.find_element_by_xpath(devXpath).click()

        # 検索に文字入力
        searchBox = "/html/body/div[1]/table/tbody/tr/td[3]/form/div/input"
        subject = "【Wow! manager】二段階認証ワンタイムキー"
        firefox.find_element_by_xpath(searchBox).send_keys(subject)

        # 3分待つ
        sleep(60)
        print("ワンタイムパスワード待ち...1分経過")
        sleep(60)
        print("ワンタイムパスワード待ち...2分経過")
        sleep(60)
        print("ワンタイムパスワード待ち...3分経過")
        print("start！！")

        searchButton = "/html/body/div[1]/table/tbody/tr/td[3]/form/div/button"
        firefox.find_element_by_xpath(searchButton).click()

        # linkText = '<img src="https://static.cybozu.com/m/5.4.6.110-20190118/image/mail20.png">'+"\n"+'【Wow! manager】二段階認証ワンタイムキー'
        mailIndexs = firefox.find_element_by_link_text(subject)
        mailIndexs.click()

        mailText = firefox.find_element_by_tag_name("tt").text

        mailTextArr = mailText.split("\n")

        # ワンタイムキー取得
        print(mailTextArr[6]+"："+mailTextArr[7])

        firefox.close()

        return mailTextArr[7]


# 起動
WowmaItemDelete().execute()

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
