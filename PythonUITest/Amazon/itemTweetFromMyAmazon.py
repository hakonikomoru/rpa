# -*- coding: utf-8 -*-
import requests
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc import Client, WordPressPost
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from pages import MyAmazonPage
from pages import TwitterLoginPage
import chromedriver_binary

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# twitterLoginPage = TwitterLoginPage(driver)
# twitterLoginPage.open()
# twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = MyAmazonPage(driver)
amazonPage.open()

for num in range(15):
    amazonPage.商品画面をURLで直接開く(
        'https://www.amazon.co.jp/s?i=merchant-items&me=AO3JD7ELZ9RTY&page='+str(num+1))
    itemsTags = amazonPage.商品一覧からClassNamedでDOMをとる("a-link-normal")
    asins = []
    for itemsTag in itemsTags:
        try:
            if "/dp/" in itemsTag.get_attribute("href"):
                # ASINだけを抜く
                asins.append(
                    {
                        "asin": str(itemsTag.get_attribute(
                            "href").split('/dp/')[1].split('/')[0]),
                        "title": itemsTag.find_element_by_tag_name(
                            "img").get_attribute("alt")
                    }
                )
        except:
            continue

    skips = []
    for asin in asins:
        if asin["asin"] not in skips:
            # 値段をとってきたい 画像をとってきたい
            print(asin["asin"])
            # 短縮するAmazonURL生成を入れる
            longUrl = "https://www.amazon.co.jp/dp/"+asin["asin"] + \
                "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22&aod=1"

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

            wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
                        "syokkotan@gmail.com", "kenyuka128")
            post = WordPressPost()
            titleSplit = asin["title"]
            splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
                      '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】']
            for split in splits:
                if split in titleSplit:
                    titleSplit = titleSplit.replace(split, ' ')
            categorys = ["プレってる", "品薄商品", "品薄"]
            categorys = categorys+titleSplit.split()
            title = asin["title"]
            post.title = title+"\n#amazon #"+' #'.join(categorys)
            post.content = title+"\n商品リンク： "+createUrl
            post.terms_names = {'category': categorys}
            post.post_status = 'publish'
            wp.call(NewPost(post))
            dt_now = datetime.datetime.now()
            postDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
            print("投稿時間： "+postDateTime)
            skips.append(str(asin["asin"]))

    # amazonPage.商品画面をURLで直接開く('https://www.amazon.co.jp/dp/'+asin)
    # amazonPage.Twitterボタンを押下()
    # amazonPage.ツイートボタンを押下()
print("次回スキップするASIN▼\n")
print(skips)

amazonPage.close()


# 機種依存文字系　https://qiita.com/sta/items/848e7a8c4699a59c604f
