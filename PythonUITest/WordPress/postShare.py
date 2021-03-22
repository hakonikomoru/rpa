# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import WordPressLoginPage
import chromedriver_binary
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import requests

# 値段をとってきたい
# 画像をとってきたい

wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
            "syokkotan@gmail.com", "kenyuka128")
post = WordPressPost()

# URLを短縮する
longUrl = "https://amazon.co.jp/gp/product/B08X5NTJSR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22&aod=1"
url = 'https://api-ssl.bitly.com/v3/shorten'
access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
query = {
    'access_token': access_token,
    'longurl': longUrl
}
createUrl = requests.get(url, params=query).json()['data']['url']


title = "ポケモンセンターオリジナル スマートフォンショルダー POKÉMON WITH YOUR CHUMS! ポケモン(Pokemon) "
post.title = title
post.content = createUrl+"\n#amazon"
post.terms_names = {'category': ["プレってる", "品薄商品"]}
post.post_status = 'publish'
wp.call(NewPost(post))

# ------------------------ゴミ▼
# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
# wordPressLoginPage = WordPressLoginPage(driver)
# wordPressLoginPage.open()
# wordPressLoginPage.ログイン("syokkotan@gmail.com", "kenyuka128")
# wordPressLoginPage.投稿を開く()
# wordPressLoginPage.投稿する()
# sleep(1000)
# wordPressLoginPage.close()
