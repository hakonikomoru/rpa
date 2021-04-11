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


# URLを短縮する
# longUrl = "https://amazon.co.jp/gp/product/B08X5NTJSR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22&aod=1"
# url = 'https://api-ssl.bitly.com/v3/shorten'
# access_token = '2c1124e977a63e564cbd29ff563de3bf01767296'
# query = {
#     'access_token': access_token,
#     'longurl': longUrl
# }
# createUrl = requests.get(url, params=query).json()['data']['url']

wp = Client('https://premieritem.wpcomstaging.com/xmlrpc.php',
            "syokkotan", "kenyuka128")
post = WordPressPost()
title = "テスト"
post.title = title
post.content = "aaa"
# post.content = "<h2>"+createUrl+"\n#amazon</h2>"
# post.content = '<a href="https://kostrivia.com/531.html">Google</>'
# post.description = 'This is the body of my new post.'
# post.tags = 'test, firstpost'
post.terms_names = {'category': ["プレってる", "品薄商品"]}
# post.post_status = 'publish'
post.post_status = 'draft'
wp.call(NewPost(post))
# 試す
# https://qiita.com/mima_ita/items/968f22f54c3febd5360f
