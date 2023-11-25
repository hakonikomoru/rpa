# coding:utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import datetime
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc import Client, WordPressPost
import tweepy
import config

class MyAmazonPage(BasePage):

    def __init__(self, driver):
        # 認証に必要なキーとトークン
        API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
        API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
        ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
        ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'
        # APIの認証
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        url = "https://www.amazon.co.jp/s?me=AO3JD7ELZ9RTY&marketplaceID=A1VC38T7YXB528"
        self.domain = '.co.jp'
        self.postTweetCount = 0
        self.skips = []
        super().__init__(driver=driver, url=url)

    def get_class_named_elements_from_product_list(self, className):
        return self.driver.find_elements_by_class_name(className)

    def get_class_named_elements_from_product_listセレクター版(self, className):
        return self.driver.find_elements_by_css_selector(className)

    def open_product_page_directly_by_url(self, url):
        self.driver.get(url)

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

        handleArray = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handleArray[0])
    
    def wait_check(self):
        one_hour = 3600
        current_time = datetime.datetime.now()
        hour = current_time.hour
        golden_hours = {7, 8, 9, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23}

        if hour in golden_hours:
            if self.goldenTimeComment != "現在は（通勤/ランチ/帰宅中・帰宅後）のゴールデンタイム":
                self.goldenTimeComment = "現在は（通勤/ランチ/帰宅中・帰宅後）のゴールデンタイム"
                print(self.goldenTimeComment)
        else:
            hours_to_wait = {
                0: 7,
                1: 6,
                2: 5,
                3: 4,
                4: 3,
                5: 2,
                6: 1,
                10: 1,
                15: 2
            }.get(hour, 0)
            
            if hours_to_wait > 0:
                print(f"今{hour}時")
                print(f"{hours_to_wait}時間後投稿開始")
                sleep(one_hour * hours_to_wait)

    def wait_for_three_hrs_for_300_posts(self):
        print("3時間以内に300件投稿を行いました")
        print("3時間休憩🍵入ります...")
        
        for i in range(1, 7):
            sleep(1800)
            elapsed_time = i * 30
            if elapsed_time < 180:
                print(f"{elapsed_time}分経過休憩🍵...")
            else:
                print("3時間休憩🍵終了！")

    def post_vertical_page_product(self, url, aod):
        # Twitterオブジェクトの生成
        self.tweet_company_sales_items(url)
        print("次回スキップするASIN▼\n")
        print(self.skips)
        # 機種依存文字系　https://qiita.com/sta/items/848e7a8c4699a59c604f

    def post_given_asin_product(self, asins, domain, aod):
        skips = []
        for num in range(15):
            for asin in asins:
                if asin["asin"] not in skips:
                    # TODO値段をとってきたい 画像をとってきたい

                    titleSplit = asin["title"]
                    splits = [
                        '〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨',
                        '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥',
                        '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰',
                        '♯', '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠',
                        '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋',
                        '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')',
                        '（', '）', '/', '【', '】', '[', ']'
                    ]
                    for split in splits:
                        if split in titleSplit:
                            titleSplit = titleSplit.replace(split, ' ')
                    categorys = ["プレってる"]
                    # "Amazonセール", "セール", "セール商品",
                    # "新生活", "新生活セール", "新生活応援", 
                    # ハッシュタグを入れたい場合は入れる↓
                    # categorys = categorys+titleSplit.split()

                    if not asin["title"]:
                        continue

                    title = asin["title"]
                    # ハッシュタグを入れたい場合は入れる↓
                    title = asin["title"]+'\n#'+' #'.join(categorys)

                    if len(title) > 140:
                        title = title[:-(len(title)-140)]

                    dt_now = datetime.datetime.now()
                    postDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
                    print("ーーーーーーーーーーーーーーー")
                    print(asin["title"])
                    print(asin["asin"])
                    print("投稿時間： "+postDateTime)
                    print("ーーーーーーーーーーーーーーー")
                    skips.append(asin["asin"])
                    # self.append_to_file(
                    #     '/Users/ebata/UITest/PythonRpa/outPutFile/urls.csv', [asin["asin"]])
                    # amazonPage.open_product_page_directly_by_url('https://www.amazon.co.jp/dp/'+asin)
                    # amazonPage.click_twitter_button()
                    # amazonPage.click_tweet_button()
        print("次回スキップするASIN▼\n")
        print(skips)
        # 機種依存文字系　https://qiita.com/sta/items/848e7a8c4699a59c604f


    def append_to_file(self, path, mergeArr):
        # pathのファイルへ書き込む
        with open(path, mode='a') as f:
            for text in mergeArr:
                f.write(str(text)+"\n")


    def clean_title(self, title):
        splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯', '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']']
        for split in splits:
            if split in title:
                title = title.replace(split, ' ')
        return title

    def create_tweet_content(self, title, categorys, url):
        hashtags = "\n#" + " #".join(categorys)
        minusCount = len(hashtags)

        if len(title) > 140 - minusCount:
            title = title[:-(len(title) - 140) - minusCount]

        return title + hashtags + "\n" + url

    def post_tweet(self, asin):
        if asin["asin"] not in self.skips:
            # 短縮するAmazonURL生成を入れる
            #アフィリなし
            # longUrl = f"https://www.amazon{self.domain}/gp/product/{asin['asin']}"
            #アフィリあり
            longUrl = f"https://www.amazon.co.jp/gp/product/{asin['asin']}/ref=as_li_qf_asin_il_tl?ie=UTF8&tag={config.affiliate_id}&creative=1211&linkCode=as2&creativeASIN={asin['asin']}"
            # longUrl = "https://www.amazon"+domain+"/gp/product/"+asin["asin"]+"/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=premierteru03-22&creative=1211&linkCode=as2&creativeASIN="+asin["asin"]
            # longUrl = "https://www.amazon"+domain+"/dp/"+asin["asin"] + \
            # "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22"+aod
            shortUrl = BasePage.shorten_url(longUrl)

            if shortUrl is None:
                return

            title = self.clean_title(asin["title"])
            if not title:
                return

            categorys = ["Amazon", "おすすめ品"]
            tweet_content = self.create_tweet_content(
                title, categorys, shortUrl
            )

            self.wait_check()
            dt_now = datetime.datetime.now()

            if self.postTweetCount > 0 and self.postTweetCount % 300 == 0:
                self.wait_for_three_hrs_for_300_posts()
            
            try:
                self.api.update_status(tweet_content)
                print("ーーーーーーーーーーーーーーー")
                print(asin["title"])
                print(asin["asin"])
                print(f"投稿時間： {dt_now.strftime('%Y-%m-%d %H:%M:%S')}")
                self.skips.append(asin["asin"])
                self.postTweetCount += 1
                print(f'現在のTweet数：{self.postTweetCount}')
                print("ーーーーーーーーーーーーーーー")

            except Exception as e:
                print(e)
                print("ーーーーーーーーーーーーーーー")

    def tweet_company_sales_items(self, url):
        for num in range(17):
            self.open_product_page_directly_by_url(url + str(num + 1))
            itemsTags = self.get_class_named_elements_from_product_list("a-link-normal")
            asins = []

            for itemsTag in itemsTags:
                try:
                    if "/dp/" in itemsTag.get_attribute("href"):
                        title = itemsTag.find_element_by_tag_name("img").get_attribute("alt")
                        print(str(itemsTag.get_attribute(
                                    "href").split('/dp/')[1].split('/')[0]))
                        
                        print(title)
                        print("ーーーーーーーーーーーーーーー")
                        asins.append(
                            {
                                "asin": str(itemsTag.get_attribute(
                                    "href").split('/dp/')[1].split('/')[0]),
                                "title": title,
                                "imageUrl": itemsTag.find_element_by_tag_name(
                                    "img").get_attribute("src")
                            }
                        )
                except:
                    continue
            
            self.goldenTimeComment = ''
            for asin in asins:
                self.post_tweet(asin)
