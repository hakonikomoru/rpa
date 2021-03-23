# まず最初に
python3の環境はpip3でインストールを行い開発環境を行ってください。
なぜかというと、pip3のほうが、pythonのライブラリが豊富ですし、日本の検索エンジンでも検索が行い安く
参考文献が簡単に出てきます。

# インストールしておくべきライブラリ（python3の実行環境が出来上がっている前提）
python3のインストール

```
% python3 -m pip install pillow
```

# インストールしておくべきライブラリ（python3の実行環境が出来上がっている前提）
seleniumのインストール

```
% pip3 install selenium 
```

chromedriver-binaryインストール
```
pip3 install chromedriver-binary

# Chromeとバージョンが最新と合わない場合、バージョン指定してインストールできる
# 現在リリースされているchromedriver-binaryのバージョンは下記にて確認が可能
# https://pypi.org/project/chromedriver-binary/#history

pip3 install chromedriver-binary==89.0.4389.23.0
```

WordPressに投稿を行ってくれるライブラリ

```
% pip3 install python-wordpress-xmlrpc
```

APIリクエストを行えるライブラリ
今現在はbitlyのAPIで、URLを短縮するのに使用している
https://pypi.org/project/requests/
```
% pip3 install requests
```

pythonAmazonSPAPI　最強かも
https://github.com/saleweaver/python-amazon-sp-api
```
% pip3 install python-amazon-sp-api
```

フォーマッターを導入
https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb