# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from BasePage import BasePage
import datetime
import requests
import tweepy


class MyAmazonPage(BasePage):

    def __init__(self, driver):
        url = "https://www.amazon.co.jp/s?me=AO3JD7ELZ9RTY&marketplaceID=A1VC38T7YXB528"
        super().__init__(driver=driver, url=url)

    def get_class_named_elements_from_product_list(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)

    def get_class_named_elements_from_product_listセレクター版(self, className):
        return self.driver.find_element(By.CSS_SELECTOR, className)

    def open_product_page_directly_by_url(self, url):
        self.driver.get(url)

    def click_twitter_button(self):
        aTags = self.driver.find_elements(By.TAG_NAME, "a")
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
        spanTags = self.driver.find_elements(By.TAG_NAME, "span")

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
        onehour = 3600
        today = datetime.datetime.now()
        hour = today.hour
        if (hour >= 7 and hour <= 9) or (hour >= 11 and hour <= 14) or (hour >= 17 and hour <= 23):
            print("現在は（通勤/ランチ/帰宅中・帰宅後）のゴールデンタイム")
        else:  
            if hour == 0:
                print("今"+str(hour)+"時")
                print("7時間後投稿開始")
                sleep(onehour*7)
            elif hour == 1:
                print("今"+str(hour)+"時")
                print("6時間後投稿開始")
                sleep(onehour*6)
            elif hour == 2:
                print("今"+str(hour)+"時")
                print("5時間後投稿開始")
                sleep(onehour*5)
            elif hour == 3:
                print("今"+str(hour)+"時")
                print("4時間後投稿開始")
                sleep(onehour*4)
            elif hour == 4:
                print("今"+str(hour)+"時")
                print("3時間後投稿開始")
                sleep(onehour*3)
            elif hour == 5 or hour == 15:
                print("今"+str(hour)+"時")
                print("2時間後投稿開始")
                sleep(onehour*2)
            elif hour == 6 or hour == 10:
                print("今"+str(hour)+"時")
                print("1時間後投稿開始")
                sleep(onehour*1)

    def wait_for_three_hrs_for_300_posts(self):
        print("3時間以内に300件投稿を行いました")
        print("3時間休憩🍵入ります...")
        sleep(1800)
        print("30分経過休憩🍵...")
        sleep(1800)
        print("60分経過休憩🍵...")
        sleep(1800)
        print("90分経過休憩🍵...")
        sleep(1800)
        print("120分経過休憩🍵...")
        sleep(1800)
        print("150分経過休憩🍵...")
        sleep(1800)
        print("3時間休憩🍵終了！")

    def post_vertical_page_product(self, url, domain, aod):
        # 認証に必要なキーとトークン
        API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
        API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
        ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
        ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'
        

        # APIの認証
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        # Twitterオブジェクトの生成
        api = tweepy.API(auth)
        skips = []
        postTweetCount = 0
        errorComment = ''
        for num in range(17):
            self.open_product_page_directly_by_url(url+str(num+1))
            itemsTags = self.get_class_named_elements_from_product_list("a-link-normal")
            asins = []
            for itemsTag in itemsTags:
                try:
                    if "/dp/" in itemsTag.get_attribute("href"):
                        title = itemsTag.find_element(By.TAG_NAME, "img").get_attribute("alt")
                        # if "ガンダム" not in title:
                        #     continue
                        # ASINだけを抜く
                        asins.append(
                            {
                                "asin": str(itemsTag.get_attribute(
                                    "href").split('/dp/')[1].split('/')[0]),
                                "title": title,
                                "imageUrl": itemsTag.find_element(By.TAG_NAME, 
                                    "img").get_attribute("src")
                            }
                        )
                except:
                    continue

            for asin in asins:
                print('現在のTweet数：'+str(postTweetCount))
                if asin["asin"] not in skips:
                    # 値段をとってきたい 画像をとってきたい
                    # 短縮するAmazonURL生成を入れる （Amazonアソシエイトの場合)
                    longUrl = "https://www.amazon"+domain+"/gp/product/"+asin["asin"]+"/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=premierteru03-22&creative=1211&linkCode=as2&creativeASIN="+asin["asin"]
                    #　非アソシエイト
                    longUrl = "https://www.amazon"+domain+"/gp/product/"+asin["asin"]

                    # longUrl = "https://www.amazon"+domain+"/dp/"+asin["asin"] + \
                    #     "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22"+aod

                    # エンドポイント
                    apiUrl = 'https://api-ssl.bitly.com/v3/shorten'
                    
                    for token in access_tokens:
                        try:
                            query = {
                                'access_token': token,
                                'longurl': longUrl
                            }
                            createUrl = requests.get(apiUrl, params=query).json()['data']['url']
                        except Exception as e:
                            print(e)
                            print("ーーーーーーーーーーーーーーー")
                            continue
                    
                    # 一時的に
                    # wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
                    #             "syokkotan@gmail.com", "kenyuka128")
                    # post = WordPressPost()

                    titleSplit = asin["title"]
                    splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
                              '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']']
                    for split in splits:
                        if split in titleSplit:
                            titleSplit = titleSplit.replace(split, ' ')
                    # ハッシュタグを入れたい場合は入れる↓
                    # categorys = categorys+titleSplit.split()

                    if not asin["title"]:
                        continue

                    title = asin["title"]
                    # ハッシュタグを入れたい場合は入れる↓
                    # categorys = ["プレってる", "Amazon", "Amazonタイムセール祭り"]
                    # categorys = ["プレってる", "Amazon", "ガンプラ"]
                    categorys = ["プレってる", "Amazon", "おすすめ品"]
                    # categorys = ["プライムデー", "Amazon", "おすすめ品"]
                    # categorys = ["Amazon", "おすすめ品"]
                    # "Amazonセール", "セール", "セール商品",
                    # "新生活", "新生活セール", "新生活応援", 
                    hashtags = "\n#"+' #'.join(categorys)
                    minusCount = len(hashtags)

                    if len(title) > 140-minusCount:
                        # 140字から超えている文字数を引いて入れる
                        title = title[:-(len(title)-140)-minusCount]
                    # 投稿内容を仕上げる
                    updatePost = title+hashtags

                    # 一時的に
                    self.wait_check()
                    dt_now = datetime.datetime.now()

                    if postTweetCount > 0 and postTweetCount % 300 == 0:
                        self.wait_for_three_hrs_for_300_posts()
                    try:
                        # ツイートを投稿
                        api.update_status(str(updatePost)+"\n"+str(createUrl))
                        postTweetCount += 1
                    except Exception as e:
                        if "User is over daily status update limit" in str(e):
                            self.wait_for_three_hrs_for_300_posts()
                            postTweetCount = 0
                            errorComment = ''
                            print(e)
                            print("ーーーーーーーーーーーーーーー")
                        elif "duplicate" in str(e):
                            if errorComment == 'duplicate':
                                continue
                            errorComment = 'duplicate'
                            print(e)
                            print("重複した投稿内容です")
                            print("ーーーーーーーーーーーーーーー")
                        continue
                    
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

    def post_given_asin_product(self, asins, domain, aod):
        skips = []
        for num in range(15):
            for asin in asins:
                if asin["asin"] not in skips:
                    # 値段をとってきたい 画像をとってきたい
                    # 短縮するAmazonURL生成を入れる
                    longUrl = "https://www.amazon"+domain+"/gp/product/"+asin["asin"]+"/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=premierteru03-22&creative=1211&linkCode=as2&creativeASIN="+asin["asin"]
                        # longUrl = "https://www.amazon"+domain+"/dp/"+asin["asin"] + \
                        # "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22"+aod

                    # エンドポイント
                    apiUrl = 'https://api-ssl.bitly.com/v3/shorten'
                    # アクセストークン
                    access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
                    query = {
                        'access_token': access_token,
                        'longurl': longUrl
                    }
                    createUrl = requests.get(apiUrl, params=query).json()[
                        'data']['url']

                    titleSplit = asin["title"]
                    splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
                              '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']']
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
