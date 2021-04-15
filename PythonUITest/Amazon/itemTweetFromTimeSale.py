# -*- coding: utf-8 -*-
import requests
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc import Client, WordPressPost
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import AmazonTimeSalePage
from pages import TwitterLoginPage
import chromedriver_binary
import tweepy

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

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
# twitterLoginPage = TwitterLoginPage(driver)
# twitterLoginPage.open()
# twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = AmazonTimeSalePage(driver)
amazonPage.open()

amazonPage.商品画面をURLで直接開く(
    'https://www.amazon.co.jp/gp/goldbox?ref_=nav_cs_gb_4421680a68ae4ba2a5c97c993c26b5a6')
sleep(5)
urls = []

dt_now = datetime.datetime.now()
today = datetime.date.today()
# ASIN重複チェック用ファイルパス
path = '/Users/ken.ebata/work/rpa/PythonUITest/outPutFile/asins'+str(today)+'.csv'
# ASIN重複チェック用ファイルを作成して最初にdummyASINを入れておく
with open(path) as f:
    oldAsins = f.read()
if not oldAsins:
    with open(path, mode='w') as f:
        f.write("dummy")
print("タイムセールURL収集開始："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
# for num in range(5):
rangeCount = 200
for num in range(rangeCount):
    print(str(num)+"/"+str(rangeCount)+"回中")
    buttons = amazonPage.商品一覧からClassNamedでDOMをとる("a-button-inner")
    for button in buttons:
        try:
            url = str(button.find_element_by_tag_name(
                "a").get_attribute("href"))
            urls.append(url)
            # amazonPage.fileに追記(
            #     '/Users/ebata/work/rpa/PythonUITest/outPutFile/urls.csv', [url])
        except:
            continue
    amazonPage.次の画面を開く()
dt_now = datetime.datetime.now()
print("タイムセールURL収集終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))

skips = []
postCount = 0
for url in urls:
    if "/dp/" in url:
        continue
    amazonPage.商品画面をURLで直接開く(url)
    itemsTags = amazonPage.商品一覧からClassNamedでDOMをとる("a-link-normal")
    asins = []
    dt_now = datetime.datetime.now()
    print("ASIN収集開始："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    for itemsTag in itemsTags:
        try:
            if "/dp/" in itemsTag.get_attribute("href"):
                # ASINだけを抜く
                asin = str(itemsTag.get_attribute(
                    "href").split('/dp/')[1].split('?')[0])
                asin = str(asin.split('/')[0])
                imageUrl = itemsTag.find_element_by_tag_name("img").get_attribute("src")
                # amazonPage.fileに追記(
                #     '/Users/ebata/work/rpa/PythonUITest/outPutFile/asins.csv', [asin])
                asins.append(
                    {
                        "asin": str(asin),
                        "title": itemsTag.get_attribute("title"),
                        "imageUrl": imageUrl
                    }
                )
                print(asin+"："+str(itemsTag.get_attribute("title")))
                print("画像URL："+str(imageUrl))
        except:
            continue

    dt_now = datetime.datetime.now()
    print("ASIN収集終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    
    for asin in asins:
        if asin["asin"] not in skips:
            # 値段をとってきたい 画像をとってきたい
            # 短縮するAmazonURL生成を入れる
            longUrl = "https://www.amazon.co.jp/gp/product/"+asin["asin"]+"/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=premierteru-22&creative=1211&linkCode=as2&creativeASIN="+asin["asin"]
            # longUrl = "https://www.amazon.co.jp/dp/"+asin["asin"] + \
            #     "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22"
            # &aod=1"

            # エンドポイント
            apiUrl = 'https://api-ssl.bitly.com/v3/shorten'
            # アクセストークン
            access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
            query = {
                'access_token': access_token,
                'longurl': longUrl
            }
            createUrl = requests.get(apiUrl, params=query).json()['data']['url']

            wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
                        "syokkotan@gmail.com", "kenyuka128")
            post = WordPressPost()
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
            categorys = ["Amazon", "タイムセール", "プレってる"]
            hashtags = "\n#"+' #'.join(categorys)
            minusCount = len(hashtags)

            if len(title) > 140-minusCount:
                # 140字から超えている文字数を引いて入れる
                title = title[:-(len(title)-140)-minusCount]
            # 投稿内容を仕上げる
            updatePost = title+hashtags

            post.title = updatePost
            # ハッシュタグを入れたい場合は入れる↓
            # post.content = title+"\n商品リンク： "+createUrl
            post.content = "商品リンク： "+createUrl+"\n"+asin["imageUrl"]
            post.terms_names = {'category': categorys}
            # 投稿URL
            # post.slug = '自分のサイトのURL'
            # サムネイルの指定
            # post.thumbnail = ここに画像のIDを指定する
            post.post_status = 'publish'

            if postCount > 0 and postCount % 300 == 0:
                print("3時間以内に300件投稿を行いました")
                print("3時間休憩入ります...")
                sleep(1800)
                print("30分経過休憩...")
                sleep(1800)
                print("60分経過休憩...")
                sleep(1800)
                print("90分経過休憩...")
                sleep(1800)
                print("120分経過休憩...")
                sleep(1800)
                print("150分経過休憩...")
                sleep(1800)
                print("3時間休憩終了！")
            try:
                # ツイートを投稿
                api.update_status(str(updatePost)+"\n"+str(createUrl))
                postCount = postCount+1
                wp.call(NewPost(post))
                dt_now = datetime.datetime.now()
            except Exception as e:
                print(e)
                if "User is over daily status update limit" in str(e):
                    print("3時間以内に300件投稿を行いました")
                    print("3時間休憩入ります...")
                    sleep(1800)
                    print("30分経過休憩...")
                    sleep(1800)
                    print("60分経過休憩...")
                    sleep(1800)
                    print("90分経過休憩...")
                    sleep(1800)
                    print("120分経過休憩...")
                    sleep(1800)
                    print("150分経過休憩...")
                    sleep(1800)
                    print("3時間休憩終了！")
                    postCount = 0
                elif "duplicate" in str(e):
                    print("重複した投稿内容です")
             
            postDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
            print("投稿時間： "+postDateTime)
            print("商品名： "+asin["title"])
            print("ASIN： "+asin["asin"])
            # ファイルへ一度投稿したASINを追記しておく
            with open(path, mode='a') as f:
                f.write(","+str(asin["asin"]))

            # 重複チェック用ファイルを閲覧して重複をなくして再度skipsに格納
            with open(path) as f:
                oldAsins = f.read()
                skips = list(set(oldAsins.split(',')))

    # amazonPage.商品画面をURLで直接開く('https://www.amazon.co.jp/dp/'+asin)
    # amazonPage.Twitterボタンを押下()
    # amazonPage.ツイートボタンを押下()
    amazonPage.次の画面を開く()

amazonPage.close()