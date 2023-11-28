import datetime

# 認証に必要なキーとトークン
API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAANWLNwEAAAAA8DwLB3bUyh0wyzuaeUEWpnSXMvs%3DXwlYPnrweEtjHRROpdEUqJwYZX97U3sm4cgTA7A2PNOR2gPX80'

affiliate_id = 'premierter0ad-22'
today = datetime.date.today()
titles_path = '/Users/ebata/work/rpa/PythonRpa/outPutFile/titles.csv'
skipTitlesPath = '/Users/ebata/work/rpa/PythonRpa/outPutFile/skipTitles.csv'

# タイムセールで閲覧するページ数
timesale_watch_page_count = 5

skip_titles = [
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

# bitlyURL短縮サービスアクセストークン
access_tokens = [
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
    '8fd3b8ae8fca6b53b5bda1ef01b831e8bbd822fe',
    '3fca34bfd616250ea93280813dedcba822ee579e',
    '98b80f63202058603f3c638440e59c7918bedce0',
    'ed901d473fc56bfa7fabcf4364a16d2f40f0b9b4'
]