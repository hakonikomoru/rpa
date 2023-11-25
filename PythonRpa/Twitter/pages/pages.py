# coding:utf-8
import requests
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link text'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'
import os


class TwitterLoginPage(BasePage):
    def __init__(self, driver):
        url = "https://twitter.com/login"
        super().__init__(driver=driver, url=url)

    def Twitterlogin(self, userName, passWord):
        sleep(10)
        # search = self.driver.find_element_by_name("session[username]")
        # search.send_keys(userName)
        # search = self.driver.find_element_by_name("session[password]")
        # search.send_keys(passWord)
        # search.send_keys(Keys.ENTER)
        search = self.driver.find_element_by_name("username")
        search.send_keys(userName)
        search.send_keys(Keys.ENTER)
        sleep(5)
        search = self.driver.find_element_by_name("password")
        search.send_keys(passWord)
        sleep(5)
        # 自分でろぐいんButtonを押す
        # self.driver.find_element_by_link_text('login').click()
        # search.send_keys(Keys.ENTER)


class TwitterPage(BasePage):
    def __init__(self, driver):
        url = 'https://twitter.com/search?q=%E7%9B%B8%E4%BA%92%E3%83%95%E3%82%A9%E3%83%AD%E3%83%BC&src=typed_query&f=user'
        super().__init__(driver=driver, url=url)

    def get_class_named_elements_from_product_list(self, className):
        return self.driver.find_elements_by_class_name(className)

    def open_product_page_directly_by_url(self, url):
        self.driver.get(url)

    def フォローアカウントリストを開く(self, target):
        self.driver.get(
            'https://twitter.com/search?q='+target+'&src=typed_query&f=user'
        )

    def 最新ツイート検索(self, keyword):
        self.driver.get(
            'https://twitter.com/search?q='+keyword+'&src=typeahead_click&f=live'
        )

    def プレってるフォローリスト(self):
        self.driver.get(
            'https://twitter.com/premier_teru/following'
        )

    def プレってるフォロワーリスト(self):
        self.driver.get(
            'https://twitter.com/premier_teru/followers'
        )

    def カンのフォロワーリスト(self):
        self.driver.get(
            'https://twitter.com/NoGucci110/followers'
        )

    def けんちゃんねるのフォロワーリスト(self):
        self.driver.get(
            'https://twitter.com/ken_channel_nel/followers'
        )

    def けんちゃんねるのフォローリスト(self):
        self.driver.get(
            'https://twitter.com/ken_channel_nel/followers'
        )

    def フォロワーリストを開く(self, twitterId):
        self.driver.get(
            'https://twitter.com/'+twitterId+'/following'
        )
        sleep(5)

    def 非相互フォローのフォロー解除する(self, scrollCount):
        for num in range(scrollCount):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(1)
        
        sleep(5)
        focuss = self.driver.find_elements_by_class_name('css-901oao')
        for focus in focuss:
            print(focus)
            try:
                if focus.get_attribute("class") == 'css-901oao' and 'フォロー中' in focus.text:
                    followerLists = focus.find_element_by_tag_name(
                        'div').find_elements_by_tag_name('div')
                    for followerList in followerLists:
                        if 'position: absolute; width: 100%; transform: translateY(' not in followerList.get_attribute("style"):
                            continue
                        if "フォローされています" == followerList.find_elements_by_tag_name('span')[3].text:
                            continue
                        divs = followerList.find_elements_by_tag_name('div')
                        for unfollower in divs:
                            try:
                                if "-unfollow" in unfollower.get_attribute("data-testid"):
                                    unfollower.click()
                                    spans = self.driver.find_elements_by_tag_name(
                                        'span')
                                    for span in spans:
                                        if "フォロー解除" in span.text:
                                            span.click()
                                            print('フォロー解除しました')
                            except:
                                continue
            except:
                continue

    def 非相互フォロワーをフォロー解除する(self, scrollCount):
        for num in range(scrollCount):
            print("スクロール："+str(num+1)+"回")
            self.driver.execute_script('window.scroll(0,1000000)')
            sleep(1)
        
        sleep(5)
        focuss = self.driver.find_elements_by_class_name('css-1dbjc4n')
        for focus in focuss:
            try:
                if focus.get_attribute("class") == 'css-1dbjc4n' and 'フォロー中' in focus.text:
                    followerLists = focus.find_element_by_tag_name(
                        'div').find_elements_by_tag_name('div')
                    for followerList in followerLists:
                        if 'position: absolute; width: 100%; transform: translateY(' not in followerList.get_attribute("style"):
                            continue
                        if "フォローされています" == followerList.find_elements_by_tag_name('span')[3].text:
                            continue
                        divs = followerList.find_elements_by_tag_name('div')
                        for unfollower in divs:
                            try:
                                if "-unfollow" in unfollower.get_attribute("data-testid"):
                                    unfollower.click()
                                    spans = self.driver.find_elements_by_tag_name(
                                        'span')
                                    for span in spans:
                                        if "フォロー解除" in span.text:
                                            span.click()
                                            print('フォロー解除しました')
                            except:
                                continue
            except:
                continue

    def 表示されたユーザーリストをフォローする(self):
        sleep(10)
        count = 0
        for scrollCount in range(1):
            for scrollCount in range(30):
                wait = WebDriverWait(self.driver, 20)
                # 指定された要素(検索テキストボックス)が表示状態になるまで待機する
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (By.CLASS_NAME, "css-1dbjc4n")
                    )
                )
                print("スクロール："+str(scrollCount+1)+"回")
                self.driver.execute_script('window.scroll(0,1000000)')
                sleep(1)

            for n in range(50):
                # 24時間でフォローは1000件までなので
                # 1時間に一回起動するので1時間でフォローできる上限は41件
                if count == 41:
                    break
                # print("ちょいスクロール")
                # self.driver.execute_script('window.scroll(0,0)')
                # for nn in range(10):
                #     self.driver.execute_script('window.scroll(0,15000)')
                self.driver.execute_script('window.scroll(0,100000)')
                spanTags = self.driver.find_elements_by_tag_name("span")
                for spanTag in spanTags:
                    try:
                        if "フォロー" == spanTag.text:
                            spanTag.click()
                            count = count + 1
                            print('フォローしました' + str(count))
                            break
                    except:
                        continue

    def 表示されたツイートをいいねする(self):
        sleep(10)
        count = 0
        for scrollCount in range(1):
            for scrollCount in range(30):
                wait = WebDriverWait(self.driver, 20)
                # 指定された要素(検索テキストボックス)が表示状態になるまで待機する
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (By.CLASS_NAME, "css-1dbjc4n")
                    )
                )
                print("スクロール："+str(scrollCount+1)+"回")
                self.driver.execute_script('window.scroll(0,1000000)')
                sleep(1)

            for n in range(50):
                # 24時間でフォローは1000件までなので
                # 1時間に一回起動するので1時間でフォローできる上限は41件
                if count == 41:
                    break
                # print("ちょいスクロール")
                # self.driver.execute_script('window.scroll(0,0)')
                # for nn in range(10):
                #     self.driver.execute_script('window.scroll(0,15000)')
                self.driver.execute_script('window.scroll(0,100000)')
                spanTags = self.driver.find_elements_by_tag_name("span")
                for spanTag in spanTags:
                    try:
                        if "フォロー" == spanTag.text:
                            spanTag.click()
                            count = count + 1
                            print('フォローしました' + str(count))
                            break
                    except:
                        continue

    def click_twitter_button(self):
        aTags = self.driver.find_elements_by_tag_name("a")
        for aTag in aTags:
            try:
                if "Twitterでシェアする" in aTag.get_attribute("title"):
                    aTag.click()
            except:
                continue

    def click_tweet_button(self):
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

        self.driver.close()
        handleArray = self.driver.window_handles
        self.driver.switch_to.window(handleArray[0])

    def 短縮URLを返す(self, longUrl):
        url = 'https://api-ssl.bitly.com/v3/shorten'
        access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
        query = {
            'access_token': access_token,
            'longurl': longUrl
        }
        r = requests.get(url, params=query).json()['data']['url']
        return r
