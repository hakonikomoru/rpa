# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
from BasePage import BasePage
import os


# ログイン画面操作
class AmazonPage(BasePage):

    def __init__(self, driver):
        # url = "https://www.amazon.co.jp/"
        url = "https://www.amazon.co.jp/s?k=BANDAI&pct-off=-0&sort=-salesrank&s=date-asc-rank&high-price=10000"
        super().__init__(driver=driver, url=url)

    def ログイン(self, loginId, passWord):
        self.driver.find_element_by_link_text('ログイン').click()
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('email')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        sleep(40)
        print("ログイン！！！")

    def 商品検索(self, searchWord):
        検索ボックスselector = "field-keywords"
        search = self.driver.find_element_by_name(検索ボックスselector)
        search.send_keys(searchWord)
        search.send_keys(Keys.ENTER)

    def 商品ページからClassNamedでDOMをとる(self, className):
        return self.driver.find_elements_by_class_name(className)

    def DOMを回してタグを解析して抽出リストを返す(self, elements):
        outPut = []
        for element in elements:
            divTags = element.find_elements_by_tag_name("div")
            for divTag in divTags:
                dataAsins = divTag.get_attribute("data-asin")
                if dataAsins != None and len(dataAsins) != 0:
                    outPut.append(dataAsins)
        print(outPut)
        # print('getcwd:      ', os.getcwd())
        # print('__file__:    ', __file__)
        # print('basename:    ', os.path.basename(__file__))
        # print('dirname:     ', os.path.dirname(__file__))
        return outPut

# ログイン画面操作


class USSCLoginPage(BasePage):

    def __init__(self, driver, land):
        if 'US' in land:
            url = "https://sellercentral.amazon.com/"
        elif 'JP' in land:
            url = 'https://sellercentral.amazon.co.jp/'

        super().__init__(driver=driver, url=url)

    def ログイン(self, loginId, passWord):
        self.driver.find_element_by_link_text('ログイン').click()
        # 検索語として「selenium」と入力し、Enterキーを押す。
        search = self.driver.find_element_by_name('email')
        search.send_keys(loginId)
        search = self.driver.find_element_by_name('password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        print("40秒以内にワンタイムパスワードの入力を終えてください。")
        sleep(40)
        print("入力時間終了")
        print("ログイン！！！")


class ProductSearchPage(BasePage):

    アメリカ商品登録画面URL = 'https://sellercentral.amazon.com/product-search?ref=xx_catadd_dnav_xx'
    日本商品登録画面URL = 'https://sellercentral.amazon.co.jp/product-search?ref=xx_catadd_dnav_xx'
    表示されている商品のselector = '#search-result > div:nth-child(1) > kat-box > div > section.kat-col-xs-4.search-row-title > kat-link > a'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def 商品登録画面をURLで直接開く(self, land):
        if "US" in land:
            self.driver.get(self.アメリカ商品登録画面URL)
        elif "JA" in land:
            self.driver.get(self.日本商品登録画面URL)

    def 検索キーワードを入力して検索する(self, keyWord):
        sleep(3)
        search = self.driver.find_element_by_id('katal-id-0')
        search.send_keys(keyWord)
        search.send_keys(Keys.ENTER)

    def 検索結果件数を取得(self):
        count = self.driver.find_element_by_css_selector(
            '#product-search-container > div.product-search > div > div.side-nav > div.main-content > div > div.results-header > div > div:nth-child(1)').text.split('件の')[0]
        return int(count)/10

    def 次へボタンが有効かチェックする(self):
        return bool(self.driver.find_element_by_css_selector(".next.copy-kat-button.secondary").get_property('disabled'))

    def 次へボタンを押下(self):
        if not self.次へボタンが有効かチェックする():
            self.driver.find_element_by_css_selector(
                ".next.copy-kat-button.secondary").click()

    def 商品のASINを抜き取る(self, land):
        # ASINのDOMを取得して、コンディションが含まれていない場合スキップ
        # 含まれていた場合は、出品制限が降りていることになるので、そのASINコードを取得する
        # ASINコードの取得の仕方は、まず「/db/」が入っていることを確認し入ってなかった場合はスキップ
        # 入っていた場合は、「/db/」で分割して
        # 2つ目の配列を取れば、ASINコードが抜き取れるのでその抜き取った内容を配列にいれる。
        if "US" in land:
            asinURL = "http://www.amazon.com/dp/"
        elif "JA" in land:
            asinURL = "http://www.amazon.co.jp/dp/"

        asins = []
        for n in range(100):
            # for n in range(1):
            print(str(
                n+1)+"ページ目■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            # 10行表示固定のため、9を明示的に記載
            sleep(5)
            rows = self.driver.find_elements_by_class_name('row')
            for rowDOM in rows:
                if "出品許可を申請" in rowDOM.text:
                    print("出品許可を申請あり")
                    try:
                        # 出品許可を申請のDOMを取得
                        regulationBtn = rowDOM.find_element_by_class_name(
                            'flex-end')
                        buttonATag = regulationBtn.find_element_by_tag_name(
                            'a').get_attribute("href")
                        aTag = rowDOM.find_element_by_tag_name('a')
                        print(aTag.text)
                        # http://www.amazon.com/dp/を含んでいるURLのみに抽出して配列に入れる
                        if asinURL in aTag.get_attribute("href"):
                            print(aTag.get_attribute("href"))
                            aTagText = aTag.text.replace(',', '|')
                            aTagText = aTagText.replace('"', '')
                            asins.append(aTagText+","+buttonATag)
                            break
                    except:
                        print("atagなし")

                # ASINURLのみ取得
                elif "コンディションを選択" in rowDOM.text:
                    try:
                        aTag = rowDOM.find_element_by_tag_name('a')
                        print(aTag.text)
                        # http://www.amazon.com/dp/を含んでいるURLのみに抽出して配列に入れる
                        if asinURL in aTag.get_attribute("href"):
                            print(aTag.get_attribute("href"))
                            aTagText = aTag.text.replace(',', '|')
                            aTagText = aTagText.replace('"', '')
                            asins.append(
                                aTagText+","+aTag.get_attribute("href").split('/dp/')[1])
                    except:
                        print("atagなし")

                elif "バリエーションを表示する" in rowDOM.text:
                    self.driver.find_element_by_name(
                        'keyboard_arrow_down').click()
                    # バリーエーションの中の商品DOMを取得
                    variationRows = self.driver.find_elements_by_class_name(
                        "variation-row")
                    for variationRowDOM in variationRows:
                        if "コンディションを選択" in variationRowDOM.text:
                            try:
                                aTag = variationRowDOM.find_element_by_tag_name(
                                    'a')
                                print(aTag.text)
                                # http://www.amazon.com/dp/を含んでいるURLのみに抽出して配列に入れる
                                if asinURL in aTag.get_attribute("href"):
                                    print(aTag.get_attribute("href"))
                                    aTagText = aTag.text.replace(',', '|')
                                    aTagText = aTagText.replace('"', '')
                                    asins.append(
                                        aTagText+","+aTag.get_attribute("href").split('/dp/')[1])
                            except:
                                print("atagなし")

            if self.次へボタンが有効かチェックする():
                break
            self.次へボタンを押下()
            # pageが表示されるのを待つ
            sleep(3)

        return self.配列内の重複を無くして配列を返す(asins)


class TwitterLoginPage(BasePage):
    def __init__(self, driver):
        url = "https://twitter.com/login"
        super().__init__(driver=driver, url=url)

    def Twitterログイン(self):
        sleep(5)
        search = self.driver.find_element_by_name("session[username_or_email]")
        search.send_keys("premier_teru")
        search = self.driver.find_element_by_name("session[password]")
        search.send_keys("hnhn8787")
        search.send_keys(Keys.ENTER)


class MyAmazonPage(BasePage):

    def __init__(self, driver):
        url = "https://www.amazon.co.jp/s?me=AO3JD7ELZ9RTY&marketplaceID=A1VC38T7YXB528"
        super().__init__(driver=driver, url=url)

    def 商品一覧からClassNamedでDOMをとる(self, className):
        return self.driver.find_elements_by_class_name(className)

    def 商品画面をURLで直接開く(self, url):
        self.driver.get(url)

    def Twitterボタンを押下(self):
        aTags = self.driver.find_elements_by_tag_name("a")
        for aTag in aTags:
            try:
                if "Twitterでシェアする" in aTag.get_attribute("title"):
                    aTag.click()
            except:
                continue

    def ツイートボタンを押下(self):
        sleep(5)
        # タブを見るカーソルが変わっていないため、一度タブを切り替える
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(self.driver.window_handles[1])
        spanTags = self.driver.find_elements_by_tag_name("span")

        for spanTag in spanTags:
            try:
                if "ツイートする" in spanTag.text:
                    spanTag.click()
                    break
            except:
                continue

        handleArray = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handleArray[0])
