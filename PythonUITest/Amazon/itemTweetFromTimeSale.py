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

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
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
print("タイムセールURL収集開始："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
for num in range(368):
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
                # amazonPage.fileに追記(
                #     '/Users/ebata/work/rpa/PythonUITest/outPutFile/asins.csv', [asin])
                asins.append(
                    {
                        "asin": str(asin),
                        "title": itemsTag.get_attribute("title")
                    }
                )
                print(asin)
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
            categorys = ["Amazon", "タイムセール", "プレってる"]
            # ハッシュタグを入れたい場合は入れる↓
            # categorys = categorys+titleSplit.split()

            if not asin["title"]:
                continue

            title = asin["title"]
            # ハッシュタグを入れたい場合は入れる↓
            title = asin["title"]+'\n#'+' #'.join(categorys)

            if len(title) > 140:
                title = title[:-(len(title)-140)]

            post.title = title
            # ハッシュタグを入れたい場合は入れる↓
            # post.content = title+"\n商品リンク： "+createUrl
            post.content = "商品リンク： "+createUrl
            post.terms_names = {'category': categorys}
            # 投稿URL
            # post.slug = '自分のサイトのURL'
            # サムネイルの指定
            # post.thumbnail = ここに画像のIDを指定する
            post.post_status = 'publish'
            wp.call(NewPost(post))
            dt_now = datetime.datetime.now()
            postDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
            print("投稿時間： "+postDateTime)
            print("商品名： "+asin["title"])
            print("ASIN： "+asin["asin"])
            skips.append(asin["asin"])

    # amazonPage.商品画面をURLで直接開く('https://www.amazon.co.jp/dp/'+asin)
    # amazonPage.Twitterボタンを押下()
    # amazonPage.ツイートボタンを押下()
    amazonPage.次の画面を開く()


print("次回スキップするASIN▼\n")
print(skips)

amazonPage.close()


# 機種依存文字系　https://qiita.com/sta/items/848e7a8c4699a59c604f
# input()　コマンドで入力ができるらしい
