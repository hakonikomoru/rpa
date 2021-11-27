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
from webdriver_manager.chrome import ChromeDriverManager

# 認証に必要なキーとトークン
API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'

# bitlyURL短縮サービスアクセストークン
accessTokens = [
    '5fc83f45d2c1872af10a5a2f55275f94f8b04ca2',
    '405d983e1fe050a09f968c100dae759bd812bdc2',
    'afde27fce5eb37239e25733ed653e9544cd568b3',
    '2c1124e977a63e564cbd29ff563de3bf01767296',
    'fd03fa9f33f45661eeb81b51b6cc6f21fb8e50bb',
    '710dab5ea21bb0f07a1f2952b5674bda4e10c32d',
    '6e0118e77bf98f7924704918bfecdc77397b0137',
    '3d2f541a6a4b211c5d491071dd1bb70f082ec6c2',
    '326473305084a4382d9f8d393fd94cdb7f981e89',
    '53956277fe16358e02af166e309c7007028d6e36',
    'ff01f1be4d93707d708e955ea07bf814a3087758',
    'c37b5c181239aee45fcaea005c6c762139bc49fb',
    '14c7ce4d141e314bff5c37fcfabc0f25ee47a3c9',
    '28403cd715c99150c913fbc7a531455140dc6ab0',
    '0378edf91a7379d87bfad612ec8fbfdfead69d42',
    'c2446a138944a345a808064308cd76c7780ab65b',
    '82b5e1b63a1ba944d9083cd2582e4b53510fea19',
    '4a8db5e27fdb07628c92a06e2cd8cafea4b3269d',
    'e1f5aa0d41c81e192724501d7baee3f09cf01365',
    '3e42fe4a7702d6c160ba4d6b463243e92b86b5b1',
    '467628cb88fd89e3cb58b9adac9f97d6c8d6e83d',
    'e07e0082969b33646175a40294dc36869d6ef659',
    '32996700c70ffc79be8d41a67184a66130cc2c6d',
    '4e2320a85efd59631a3afbe0da4d8647d97daadc',
    'b1e1bf635021a2279a7d0d837439ce1100b34ab5',
    'fd1b8e61ea666ecd93e992deaad7ef9cdafc8c7b',
    '8fd3b8ae8fca6b53b5bda1ef01b831e8bbd822fe'
]

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Twitterオブジェクトの生成
api = tweepy.API(auth)

# options = Options()
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
# twitterLoginPage = TwitterLoginPage(driver)
# twitterLoginPage.open()
# twitterLoginPage.Twitterログイン("premier_teru", "hnhn8787")
amazonPage = AmazonTimeSalePage(driver)
amazonPage.open()

#Twitterトレンドを見てハッシュタグを調整しよう
amazonPage.商品画面をURLで直接開く(
    'https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fprimeday%3Fref_%3Dnav_custrec_signin%26_encoding%3DUTF8&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
)
amazonPage.ログイン('k.ebata.mail@gmail.com', 'hnhn8787')

amazonPage.商品画面をURLで直接開く(
    'https://www.amazon.co.jp/gp/goldbox/all-deals/?ie=UTF8&ref_=sv_whd_1'
    # 'https://www.amazon.co.jp/gp/goldbox?ref_=nav_cs_gb_4421680a68ae4ba2a5c97c993c26b5a6'　消すかも
    # 'https://www.amazon.co.jp/b/ref=gwd_hero?node=4160355051&pf_rd_r=NC6R46MSH08EDKK6VWJT&pf_rd_p=c11b0870-7e30-4bc2-9467-2c8402e138b6'　消すかも
    # 'https://www.amazon.co.jp/b/ref=gwd_hero/?_encoding=UTF8&node=4160355051&pf_rd_r=1T772RNXZWK3BYAAVKBG&pf_rd_p=0150b865-c401-4073-bf04-4f8a988f7f51&pd_rd_r=1823c1c1-3015-46ec-b762-462dd7353e07&pd_rd_w=ZULPL&pd_rd_wg=BjfbX&ref_=pd_gw_unk'
)

sleep(5)
urls = []

dt_now = datetime.datetime.now()
today = datetime.date.today()
# ASIN重複チェック用ファイルパス
path = '/Users/ken.ebata/work/rpa/PythonRpa/outPutFile/asins'+str(today)+'.csv'
titlesPath = '/Users/ken.ebata/work/rpa/PythonRpa/outPutFile/titles.csv'
skipTitlesPath = '/Users/ken.ebata/work/rpa/PythonRpa/outPutFile/skipTitles.csv'
# ASIN重複チェック用ファイルを作成して最初にdummyASINを入れておく
# try:
with open(path) as f:
    oldAsins = f.read()
# except:
if not oldAsins:
    with open(path, mode='w') as f:
        f.write("dummy")

# for num in range(5):
# 次のページ数
rangeCount = 200
rangeCount = 834
rangeCount = 167
# rangeCount = 20
skipTitles = [
    "スニーカー",
    "シューズ",
    "シャツ",
    "ブラウス",
    "トップス",
    "ボトムス",
    "パンツ",
    "ブリーフ",
    "ズボン",
    "ソックス",
    "半袖",
    "七分丈",
    "九分丈",
    "アパレル",
    "レディース",
    "メンズ",
    "サンダル",
    "リュック",
    "ブラジャー",
    "バッグ",
    "弁当",
    "食品",
    "中華そば",
    "ラーメン",
    "布団",
    "ラジコン",
    "ドローン",
    "パペット",
    "ベッド",
    "スマホケース",
    "時計"
]
stockTitles = [
    # ガジェット系
    "Razer", "レイザー", "Logicool", "ロジクール", "logitech", "ELECOM", "エレコム",
    "ゲーミング", "パソコン", "キャプチャーボード", "ゼンハイザー", "モニター", "デスクトップ",
    "PC", "switch", "ゲーム", "Amazon", "アマゾン", "sony", "ソニー", "Apple",
    # キャンプ系
    "アウトドア", "キャンプ", "ビール", "バーベキュー", "BBQ", "テント",
    # 夏
    "水着", "浮き輪", "夏", "プロテイン",
    # 家電
    "掃除機",
    # 日用品
    "マスク",
    "韓国","韓国コスメ"
]
notTitleCount = 0
selectorGetMissCount = 0
souCount = 0
atagAsins = []
skipAtagsAsins = []
print("タイムセールURL収集開始："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
for num in range(rangeCount):
    print(str(num+1)+"/"+str(rangeCount)+"回中")
    buttons = amazonPage.商品一覧からClassNamedでDOMをとる("a-button-inner")
    for button in buttons:
        try:
            url = button.find_element_by_tag_name("a").get_attribute("href")
            print("取得したURL："+str(url))
            urls.append(url)
            # amazonPage.fileに追記(
            #     '/Users/ebata/work/rpa/PythonRpa/outPutFile/urls.csv', [url])
        except Exception as e:
            print(e)
            print("ボタンが無いためスキップしました。")
            continue
    # ここでもう人手間！
    # aタグでidが"dealTitle"だった場合のhrefを取得
    atags = amazonPage.商品一覧からtagNameでDOMをとる("a")
    for atag in atags:
        try:
            if atag.get_attribute("id") == "dealTitle" and "/dp/" in atag.get_attribute("href"):
                asin = str(atag.get_attribute(
                    "href").split('/dp/')[1].split('?')[0])
                asin = str(asin.split('/')[0])
                if asin in skipAtagsAsins:
                    continue
                atagAsins.append(
                    {
                        "asin": str(asin),
                        "title": atag.text,
                        "imageUrl": ""
                    }
                )
                skipAtagsAsins.append(str(asin))
                print(asin)
                print(atag.text)
        except Exception as e:
            print(e)
            print("不要なaタグの為スキップしました")
            continue
    amazonPage.次の画面を開く()
dt_now = datetime.datetime.now()
print("タイムセールURL収集終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
# exit()
skipAsins = []
postCount = 0
dpInAsins = []
skipUrls = []
for url in urls:
    # ここはメソッド張ってdp含まない場合も吸い取れるようにしないとかも
    if "/dp/" in url:
        print("「/dp/」を含むURLの為スキップしました。："+str(url))
        continue
    amazonPage.商品画面をURLで直接開く(url)
    itemsTags = amazonPage.商品一覧からClassNamedでDOMをとる("a-link-normal")

    if not atagAsins:
        asins = []
    else:
        asins = atagAsins
        # 何度も入れ直してしまうのでatagAsinsはリセットする
        atagAsins = []

    dt_now = datetime.datetime.now()
    print("ASIN収集開始："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    souCount = souCount + 1
    for itemsTag in itemsTags:
        try:
            if "/dp/" in itemsTag.get_attribute("href"):
                # ASINだけを抜く
                asin = str(itemsTag.get_attribute(
                    "href").split('/dp/')[1].split('?')[0])
                asin = str(asin.split('/')[0])
                imageUrl = itemsTag.find_element_by_tag_name("img").get_attribute("src")
                asins.append(
                    {
                        "asin": str(asin),
                        "title": itemsTag.get_attribute("title"),
                        "imageUrl": imageUrl
                    }
                )
                print(asin+"："+str(itemsTag.get_attribute("title")))
                print("画像URL："+str(imageUrl))
        except Exception as e:
            selectorGetMissCount = selectorGetMissCount + 1
            print(e)
            print("selectorの取得に失敗しました。"+str(selectorGetMissCount))
            continue

    dt_now = datetime.datetime.now()
    print("ASIN収集終了："+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
    
    for asin in asins:
        # タイトル名で使用されている文言を取得
        titleSplit = asin["title"]
        splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
                    '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']','「','」']
        for split in splits:
            if split in titleSplit:
                titleSplit = titleSplit.replace(split, ' ')
        # ハッシュタグを入れたい場合は入れる↓
        # categorys = categorys+titleSplit.split()
        # ファイルへ一度投稿したASINを追記しておく
        with open(titlesPath, mode='a') as f:
            ts = str(",".join(list(set(titleSplit.split()))))
            f.write(ts)
                            
        # with open(titlesPath) as f:
        #     readTitles = f.read()
        #     skipTitles = list(set(readTitles.split(',')))

        # with open(skipTitlesPath) as f:
        #     rTs = f.read()
        #     sTs = list(set(rTs.split(',')))

        # 仮置
        # skipTitles = [
        #     "スニーカー",
        #     "シューズ",
        #     "シャツ",
        #     "ブラウス"
        # ]

        # 指定した単語を含む商品はツイートしない
        br = 0
        for skipTitle in skipTitles:
            if skipTitle in asin["title"]:
                br = 1
                break 

        if asin["asin"] in skipAsins or br == 1:
            print("投稿済みのASINのためスキップしました。")
            if br == 1:
                print("投稿をスキップしたい単語が商品名に含まれているためスキップしました。")
            continue
        # and asin["title"] not in skipTitles:
        # longUrl = "https://www.amazon.co.jp/dp/"+asin["asin"] + \
        #     "/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1&linkCode=ure&creative=6339&tag=jalcojp-1583421-22"
        # &aod=1"

        # エンドポイント
        apiUrl = 'https://api-ssl.bitly.com/v3/shorten'
        
        # 短縮するAmazonURL生成を入れる
        longUrl = "https://www.amazon.co.jp/gp/product/"+asin["asin"]+"/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=premierteru02-22&creative=1211&linkCode=as2&creativeASIN="+asin["asin"]
        for token in accessTokens:
            try:
                query = {
                    'access_token': token,
                    'longurl': longUrl
                }
                createUrl = requests.get(apiUrl, params=query).json()['data']['url']
            except Exception as e:
                print(e)
                print("短縮URLの変換上限数に達したため他のトークンを確認します。")
                continue

        try:
            wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
                        "syokkotan@gmail.com", "kenyuka128")
        except Exception as e:
            print(e)
            print("WordPressの投稿に失敗しました。")
            wp = Client('https://premieritem.wordpress.com//xmlrpc.php',
                        "syokkotan@gmail.com", "kenyuka128")
                        
        post = WordPressPost()

        # titleSplit = asin["title"]
        # splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
        #           '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']']
        # for split in splits:
        #     if split in titleSplit:
        #         titleSplit = titleSplit.replace(split, ' ')
        # # ハッシュタグを入れたい場合は入れる↓
        # # categorys = categorys+titleSplit.split()
        # # ファイルへ一度投稿したASINを追記しておく
        # with open(titlesPath, mode='a') as f:
        #     ts = str(",".join(list(set(titleSplit.split()))))
        #     f.write(ts)
                            
        # with open(titlesPath) as f:
        #     readTitles = f.read()
        #     skipTitles = list(set(readTitles.split(',')))

        if not asin["title"]:
            notTitleCount = notTitleCount + 1
            # print("タイトルがうまく取得できていないためスキップしました。"+str(notTitleCount))
            print("タイトルがうまく取得できていないためハッシュタグとサムネURLだけ投稿します"+str(notTitleCount))
            # continue

        title = asin["title"]
        # ハッシュタグを入れたい場合は入れる↓
        # categorys = ["Amazon", "タイムセール", "Amazonタイムセール祭り"]
        categorys = ["Amazon", "タイムセール", "Amazonタイムセール"]
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
            amazonPage.三百件投稿の場合三時間待機()
        try:
            # ツイートを投稿
            if createUrl in skipUrls:
                print("新しい短縮URLが取得できない為、終了します。")
                exit()
            amazonPage.待機チェック()
            api.update_status(str(updatePost)+"\n"+str(createUrl))
            # 既に投稿していた場合終了する
            # リストに入れる
            skipUrls.append(createUrl)
            postCount = postCount+1
            # WP投稿
            if asin["imageUrl"]:
                wp.call(NewPost(post))
            dt_now = datetime.datetime.now()
        except Exception as e:
            print(e)
            if "User is over daily status update limit" in str(e):
                amazonPage.三百件投稿の場合三時間待機()
                postCount = 0
            elif "duplicate" in str(e):
                print("重複した投稿内容です")
            
        postDateTime = str(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
        print("投稿時間： "+postDateTime)
        print("商品名： "+asin["title"])
        print("ASIN： "+asin["asin"])
        # 売れ筋商品はASINを記録しない
        if asin["title"] not in stockTitles:
            # ファイルへ一度投稿したASINを追記しておく
            with open(path, mode='a') as f:
                f.write(","+str(asin["asin"]))

            # 重複チェック用ファイルを閲覧して重複をなくして再度skipAsinsに格納
            with open(path) as f:
                oldAsins = f.read()
                skipAsins = list(set(oldAsins.split(',')))

    # amazonPage.商品画面をURLで直接開く('https://www.amazon.co.jp/dp/'+asin)
    # amazonPage.Twitterボタンを押下()
    # amazonPage.ツイートボタンを押下()
    amazonPage.次の画面を開く()

amazonPage.close()