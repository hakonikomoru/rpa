# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
import datetime

class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

# ログイン画面操作
class LoginPage(BasePage):

    def __init__(self, driver):
        url = "https://auctions.yahoo.co.jp/user/jp/show/mystatus"
        super().__init__(driver=driver, url=url)

    def ログイン(self, loginId, passWord):  
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('login') 
        search.send_keys(loginId)
        self.driver.find_element_by_name('btnNext').click()
        search = self.driver.find_element_by_name('passwd') 
        # wait
        self.driver.implicitly_wait(10)
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        try:
            self.driver.find_element_by_class_name("btnCancel").click()
        except:
            print("2段階認証案内画面はなし！")

# ログイン画面操作
class AppToolPage(BasePage):

    def __init__(self, driver):
        url = "https://apptool.jp/mypage"
        super().__init__(driver=driver, url=url)

    def ログイン(self, loginId, passWord):  
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('login') 
        search.send_keys(loginId)
        self.driver.find_element_by_name('btnNext').click()
        search = self.driver.find_element_by_name('passwd') 
        # wait
        self.driver.implicitly_wait(10)
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        try:
            self.driver.find_element_by_class_name("btnCancel").click()
        except:
            print("2段階認証案内画面はなし！")


# マイ・オークション画面操作
class MyAuctionPage(BasePage):

    前回の評価の内容selector = "body > table:nth-child(4) > tbody > tr > td > form:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td > b"

    def __init__(self, driver):
        super().__init__(driver=driver)
        
    def focusToElement(self, by, value, preventScroll):
        JavaScriptFocusToElement = "arguments[0].focus({'preventScroll': arguments[1]})"
        element = self.driver.find_element(by, value)
        self.driver.execute_script(JavaScriptFocusToElement, element, preventScroll)

    def 出品終了分ボタンを押下(self):  
        self.driver.find_element_by_class_name("decLinkBtn").click()

    def 終了したオークションリンクを押下(self):  
        self.driver.find_element_by_link_text("終了したオークション").click()
    
    def 出品終了分画面をURLで直接開く(self):
        self.driver.get('https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1')

    def 定形コメント入力ボタンを押下(self):
        self.driver.find_element_by_id("commonTextIn").click()

    def 青いボタンを押下(self):
        self.driver.find_element_by_class_name("libBtnBlueL").click()

    def 赤いボタンを押下(self):
        #if self.driver.find_element_by_class_name("libBtnBlueL").text != "落札者を評価する":
        print("赤いボタン押します！")
        sleep(3)
        self.driver.find_element_by_class_name("libBtnRedL").click()
        print("取引連絡と評価完了！")

    def n行目の商品名を取得(self, n):
        selector = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(6) > tbody > tr:nth-child('+str(n)+') > td:nth-child(3) > a'
        return self.driver.find_element_by_css_selector(selector).text

    def 発送連絡をして評価をする上(self):
        self.青いボタンを押下()
        self.赤いボタンを押下()
        try:
            text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
            print(str(text)+"があった模様")
        except:
            self.青いボタンを押下()
            self.定形コメント入力ボタンを押下()
            self.青いボタンを押下()
            self.青いボタンを押下()

    def 発送連絡をして評価をする下(self):
        self.青いボタンを押下()
        print("1")
        self.赤いボタンを押下()
        print("2")
        try:
            text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
            print(str(text)+"があった模様")
        except:
            self.青いボタンを押下()
            print("3")
            self.定形コメント入力ボタンを押下()
            self.青いボタンを押下()
            self.青いボタンを押下()

    def 評価をする(self):
        self.定形コメント入力ボタンを押下()
        self.青いボタンを押下()
        self.青いボタンを押下()

    def 取引連絡ボタンを押下(self):
        dt_now = datetime.datetime.now()
        print("開始時刻："+str(dt_now))
        count = len(self.driver.find_elements_by_css_selector("#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > a"))+1
        print("合計表示ページ数："+ str(count))
        for pageCount in range(count):
            pageNum = pageCount + 1
            print("ページ数："+ str(pageNum))
            if pageNum > 1:
                self.driver.get('https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1&apg='+str(pageNum))
            for n in range(50):
                oneLoopStart = datetime.datetime.now()
                num = n + 1
                print(str(num)+"roop目■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                # あとで戻る可能性があるのでここでURLを取得しておく
                curUrlFirst = self.driver.current_url
                print(str(num)+"行目------------------------------------------------------------------------------------")
                商品名 = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(6) > tbody > tr:nth-child('+str(num + 1)+') > td:nth-child(3) > a'
                print("商品名：" + self.driver.find_element_by_css_selector(商品名).text)
                # 取引連絡ボタンのselectorを生成
                selector = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(6) > tbody > tr:nth-child('+str(num + 1)+') > td:nth-child(8) > table > tbody > tr:nth-child(1) > td > a'
                # n個目の取引連絡ボタンを押下
                self.driver.find_element_by_css_selector(selector).click()

                # 取引連絡画面に入ったあたのアクション
                try:
                    self.青いボタンを押下()
                    try:
                        text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
                        print(str(text)+"があった模様")
                        self.driver.get(curUrlFirst)
                    except: 
                        print("取引連絡が必要　上")
                        self.発送連絡をして評価をする上()
                        
                except:
                    try:
                        rangeNum = self.driver.find_element_by_class_name("decTxt06").text.split('件中')[0]
                        print("落札件数　合計："+rangeNum+"件")
                        for n in range(int(rangeNum)):
                            num = n + 1
                            print("取引連絡の中の取引連絡"+str(num)+"行目の取引連絡----------------------------------------------------")
                            # あとで戻る可能性があるのでここでURLを取得しておく
                            curUrlSecond = self.driver.current_url
                            # 取引連絡ボタンのselectorを生成
                            selector = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr > td > div:nth-child(5) > table > tbody > tr:nth-child('+str(num + 1)+') > td:nth-child(5) > div.decBt01 > a'
                            try:
                                self.driver.find_element_by_css_selector(selector).click()
                            except: 
                                break
                                
                            try:
                                self.青いボタンを押下()
                                try:
                                    text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
                                    print(str(text)+"があった模様")
                                    self.driver.get(curUrlSecond)
                                except: 
                                    print("取引連絡が必要　下")
                                    self.発送連絡をして評価をする下()
                            except:
                                print("取引連絡できなそうだった！")
                            # 元の画面に戻る
                            self.driver.get(curUrlSecond)
                    except:
                        self.driver.get(curUrlSecond)
                # 元の画面に戻る
                self.driver.get(curUrlFirst)
                oneLoopEnd = datetime.datetime.now()
                print("1Loop処理時間："+str(oneLoopStart)+"~"+str(oneLoopEnd))

    def 評価ボタンを押下(self):
        count = len(self.driver.find_elements_by_css_selector("#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > a"))+1
        for pageCount in range(count):
            pageNum = pageCount + 1
            print("ページ数："+str(pageNum))
            if pageNum > 1:
                self.driver.get('https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1&apg='+str(pageNum))
            for n in range(50):
                num = n + 1
                print(str(num)+"roop目■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                # あとで戻る可能性があるのでここでURLを取得しておく
                curUrlFirst = self.driver.current_url
                # 評価ボタンのselectorを生成
                selector = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table:nth-child(6) > tbody > tr:nth-child('+str(num + 1)+') > td:nth-child(8) > table > tbody > tr:nth-child(2) > td > a'
                print(str(num)+"行目------------------------------------------------------------------------------------")
                # n個目の評価ボタンを押下
                self.driver.find_element_by_css_selector(selector).click()

                # 評価画面に入ったあたのアクション
                try:
                    self.青いボタンを押下()
                    try:
                        text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
                        print(str(text)+"があった模様")
                        self.driver.get(curUrlFirst)
                    except: 
                        print("評価が必要　上")
                        self.評価をする()
                        print("評価完了！")
                        

                except:
                    rangeNum = self.driver.find_element_by_class_name("decTxt06").text.split('件中')[0]
                    print("表示件数　合計："+rangeNum+"件")
                    for n in range(int(rangeNum)):
                        num = n + 1
                        print("評価の中の評価"+str(num)+"行目の評価----------------------------------------------------")
                        # あとで戻る可能性があるのでここでURLを取得しておく
                        curUrlSecond = self.driver.current_url
                        # 評価ボタンのselectorを生成
                        selector = '#acWrContents > div > table > tbody > tr > td > table > tbody > tr > td > div:nth-child(5) > table > tbody > tr:nth-child('+str(num + 1)+') > td:nth-child(5) > div.decBt02 > a'
                        self.driver.find_element_by_css_selector(selector).click()
                        
                        try:
                            try:
                                text = self.driver.find_element_by_css_selector(self.前回の評価の内容selector).text
                                print(str(text)+"があった模様")
                                self.driver.get(curUrlSecond)
                            except: 
                                print("評価が必要　下")
                                self.評価をする()
                                print("評価完了！")
                        except:
                            print("評価できなそうだった！")
                        # 元の画面に戻る
                        self.driver.get(curUrlSecond)
                # 元の画面に戻る
                self.driver.get(curUrlFirst)

    # 催促コメント機能追加