# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import WordPressLoginPage
import chromedriver_binary
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, DeletePost
from wordpress_xmlrpc.methods.users import GetUserInfo
import requests
import tweepy
import datetime

wp = Client('https://premieritem.wordpress.com/xmlrpc.php',
            "syokkotan", "kenyuka128")
# post = WordPressPost()
number = 100
# post_status = "draft"
post_status = "publish"
order = "ASC"
offset = 0
# order = "DESC"
for n in range(99):
    # コンテンツ取得
    contents = wp.call(GetPosts({"number": number, "offset": offset, "orderby": "post_modified", "order": order, "post_status": post_status}))
    if not contents:
        print("コンテンツが無いため終了しました。")
        break
    for content in contents:
        # コンテンツ削除
        ret = wp.call(DeletePost(content.id))
        if ret == 1:
            print("contentId:"+str(content.id)+" の投稿を削除しました。")
