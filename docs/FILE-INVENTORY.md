# ファイル一覧・役割（FILE INVENTORY）

> 生成: リポジトリ静的解析（2026-06-03）  
> 機密: API キー・パスワードの**値は記載しない**。該当ファイルは「機密直書きあり」と表記。

---

## ルート（`/Users/ebata/app/rpa/`）

| ファイル | 種別 | 役割 |
|----------|------|------|
| `README.md` | ドキュメント | Python3 / pip3、`selenium`、`chromedriver-binary`、`python-wordpress-xmlrpc`、`requests`、`python-amazon-sp-api`、`tweepy` などの導入手順 |
| `COMMAND.md` | リファレンス | Selenium の要素取得メモ（旧 API / 新 API 対応表、スクロール用 `execute_script`） |
| `TODO.md` | メモ | Amazon 検索 URL（snowpeak カテゴリ）のメモのみ |
| `get-pip.py` | ツール | pip ブートストラップ用の公式スクリプト（プロジェクトロジックとは無関係） |
| `geckodriver.log` | ログ | Firefox GeckoDriver 実行時のログ残骸（再生成可能・コミット不要推奨） |
| `AGENTS.md` | 運用 | Cursor 向け: `docs/project-sync.md` 参照・構成変更時 `npm run sync:project-docs` |
| `project.sync.config.json` | 設定 | project-sync 自動生成用（`repo`: `hakonikomoru/rpa` 等） |
| `.vscode/extensions.json` | 設定 | VS Code 推奨拡張の定義 |
| `.vscode/settings.json` | 設定 | 空ファイル |
| `.githooks/pre-commit` | Git | コミット前に `sync-project-docs` を走らせるフック（有効化は `git config core.hooksPath .githooks`） |
| `scripts/project-sync-core.mjs` | ビルド | `~/app` 共通: `project-sync.md` の自動ブロック生成コア |
| `scripts/sync-project-docs.mjs` | ビルド | 上記の CLI ラッパー（`npm run sync:project-docs`） |
| `docs/project-sync.md` | ドキュメント | AI 向けリポジトリ概要・ディレクトリツリー（自動更新ブロック付き） |
| `docs/REPOSITORY-OVERVIEW.md` | ドキュメント | 本リポジトリの目的・アーキテクチャ概要 |
| `docs/FILE-INVENTORY.md` | ドキュメント | 本ファイル |

---

## `PythonRpa/` 共通

| ファイル | 種別 | 役割 |
|----------|------|------|
| `PythonRpa/README.md` | ドキュメント | Selenium 開発環境構築の Qiita リンクのみ |
| `PythonRpa/.DS_Store` | システム | macOS フォルダメタデータ（削除可） |
| `PythonRpa/__pycache__/` | 生成物 | Python バイトコード（コミット不要推奨） |

---

## `PythonRpa/Amazon/` — Amazon せどり・ツイート自動化

### 設定・基底

| ファイル | 役割 | 備考 |
|----------|------|------|
| `config.py` | 集中設定 | **機密直書きあり**: Twitter API、Bitly トークン配列、アフィリエイト ID、`skip_titles` / `stockTitles`、CSV パス（旧 `work/rpa` パス） |
| `BasePage.py` | 基底クラス | `open`/`close`、CSV 読み書き、重複除去、`pyshorteners`（TinyURL）で URL 短縮（リトライ付き `requests`） |
| `memo.md` | メモ | 「週末はカード・スリーブ系が売れやすい」など運用メモ |

### エントリースクリプト（`python3` で直接実行）

| ファイル | 役割 | 主な依存 |
|----------|------|----------|
| `collect_sale_asins.py` | **セール ASIN 収集専用**（推奨エントリ）。`sale_asin_collector.py` を使用 | `.env` の `AMAZON_EMAIL` / `AMAZON_PASSWORD`（任意） |
| `sale_asin_collector.py` | ゴールドボックス一覧のスクロール・複数セレクタ・ページネーション・CSV 追記 | `asin_utils.py`, `paths.py` |
| `asin_utils.py` | `/dp/` 等から ASIN 抽出・重複除去 | |
| `paths.py` | `outPutFile/asins{日付}.csv` などリポジトリ内パス | |
| `itemTweetFromTimeSale.py` | ASIN 収集後、**`AMAZON_POST_TWEETS=1` のときのみ** tweepy 投稿 | 既定は収集のみ |
| `itemTweetFromMyAmazon.py` | **自店舗（merchant-items）** の商品ページを巡回しツイート投稿 | `MyAmazonPage` |
| `itemTweetDelete.py` | 指定 Twitter アカウントの **タイムラインを最大 3200 件ずつ削除**（レート制限時スリープ） | tweepy API v1, **機密直書き** |
| `itemSearch.py` | Amazon トップで検索・タグ抽出の **実験スクリプト**（出力先は別パス `UITest`） | `AmazonPage`, `ProductSearchPage` |
| `itemAddSearchFromJP.py` | **Amazon セラーセントラル JP** にログインし、キーワードリストで商品検索・ASIN 収集 | `USSCLoginPage`, `ProductSearchPage`, **機密直書き** |
| `itemAddSearchFromUS.py` | **Amazon セラーセントラル US** 版（出品制限リスト付き長大 `keyWords`） | 同上（US） |
| `titleSelection.php` | 商品タイトルから **除外・選別用キーワード配列**（数万行級の PHP 配列） | Python からは未統合。フィルタ辞書として利用想定 |

### `module/`

| ファイル | 役割 |
|----------|------|
| `ChatGPT.py` | OpenAI Completion（`text-davinci-002-ja`）の **動作確認サンプル**。`OPENAI_API_KEY` 環境変数前提 |

### `pages/` — Page Object

| ファイル | 役割 |
|----------|------|
| `AmazonPage.py` | Amazon 一般ページ: 検索、商品リストのクラス名要素取得、CSV 出力 |
| `AmazonTimeSalePage.py` | タイムセール / Black Friday URL、ログイン、ページ送り、商品抽出・ツイート文生成・投稿ロジックの中心 |
| `MyAmazonPage.py` | 自店舗一覧・商品詳細から **Twitter シェア UI 経由または API で投稿**、`config` のスキップ語・在庫タイトル判定 |
| `MyAmazonPagekyu.py` | `MyAmazonPage` の **旧版・バックアップ**（クラス名・ロジックが似る） |
| `ProductSearchPage.py` | セラーセントラル内の商品検索結果をパースし ASIN 等をファイル出力 |
| `TwitterLoginPage.py` | Amazon フロー内で使う Twitter ログイン画面操作（Amazon 配下のコピー） |
| `USSCLoginPage.py` | **Seller Central** ログイン（JP/US 切替引数） |
| `pages/__pycache__/` | 生成物 |

### `Amazon/__pycache__/`

Python コンパイル済み `.pyc`（`BasePage`, `config`, `pages` 等）。

---

## `PythonRpa/Twitter/` — X（Twitter）フォロー・検索自動化

### 共通

| ファイル | 役割 |
|----------|------|
| `BasePage.py` | 他モジュールと同型の最小 `BasePage`（`open`/`close` のみに近い） |
| `pages/pages.py` | `TwitterLoginPage`（ログイン DOM）、`TwitterPage`（検索 URL、フォロー/いいね/リスト操作の日本語メソッド名多数） |

### エントリースクリプト

| ファイル | 役割 | 特徴 |
|----------|------|------|
| `TwitterFollow.py` | tweepy **検索 API** で「相互フォロー」等のツイート作者を取得しフォロー | API キー **機密直書き**（コメントで別アカウントのキーも残存） |
| `TwitterFollowNew.py` | 検索結果からユーザー情報を **コンソール出力**（フォロー処理は軽量） | 別セットの API キー |
| `TwitterFollowKen.py` | Selenium でログイン → **特定アカウントのフォロワー一覧**からフォロー。100 回ループ＋1 時間スリープ | `ken_channel_nel` 等 |
| `TwitterFollowPremier.py` | 同上パターン、`premier_teru` アカウント向け | |
| `TwitterInteractiveFollowKen.py` | `TwitterFollowKen` と同系の **インタラクティブフォロー** バリエーション | |
| `TwitterUserFollowerFollow.py` | tweepy `followers_ids` で ID 収集後、**ブラウザでフォロー** | `NoGucci110` 等ハードコード |
| `TwitterUnFollow.py` | Selenium ログイン後 **アンフォロー** 操作 | |
| `TwitterKeywordSearchAutoLike.py` | 「おはようVtuber」等で **検索ページを開いて待機**（いいね処理は大部分コメントアウト） | 実験・未完成に近い |

---

## `PythonRpa/Mercari/` — メルカリ出品管理

| ファイル | 役割 |
|----------|------|
| `BasePage.py` | 最小 WebDriver ラッパ |
| `pages.py` | `MercariShopsPage` — メルカリ Shops の DOM 操作 |
| `MercariLogin.py` | **Google ログイン**でメルカリに入る。クラス内で `webdriver.Chrome()` を保持 | **機密直書きあり** |
| `MercariPriceChange.py` | 出品一覧を走査し **全商品を +1 円 → 元に戻す**（露出対策の典型パターン） | `MercariLogin` 利用 |
| `MercariNotSaleItemDelete.py` | 出品中で売れていない商品を **削除** | |
| `MercariItemOnlyUpdate.py` | Shops ページを開き **商品情報のみ更新**（reCAPTCHA 回避用プロファイルコメントあり） | |
| `mercariSearch.py` | メルカリ検索 URL を開く **テンプレート断片**（Selenium 公式例に近く未完成） | |
| `re.py` | Chrome **ユーザーデータディレクトリ**指定の接続テスト（URL マスク） | |

---

## `PythonRpa/PointGet/` — 楽天ポイント

| ファイル | 役割 |
|----------|------|
| `BasePage.py` | 最小基底 |
| `pages.py` | `RakutenENaviLoginPage`（楽天 e-NAVI ログイン）、`ClickDePointPage`（ページ内 `<a>` を総なめクリック） |
| `rakutenENaviClick.py` | ログイン → **クリックでポイント**系を自動クリック | **機密直書きあり**。コメントにアップツール URL |

---

## `PythonRpa/TokyoCalendarDate/` — 東京カレンダーデート

| ファイル | 役割 |
|----------|------|
| `BasePage.py` | 最小基底 |
| `actions.py` | `LoginPage` — **Facebook モバイルログイン**経由で tokyo-calendar-date.jp に接続。いいね・リスト・スクロール等の DOM 操作 |
| `autoLike.py` | 会員リストを最大 3000 人ループで **いいね**（モバイルエミュレーション headless 可） | **機密直書き** |
| `autoVote.py` | **会員審査（スクリーニング）画面で投票**（OK/NG ボタン、1000 ループ） | |
| `autoStamp.py` | 新規会員リストをスクロールし **スタンプ** 付与 | |

---

## `PythonRpa/outPutFile/` — 実行時データ（CSV）

スクリプトの **入力・出力・重複排除用** のデータ置き場。Git に多数コミットされている。

| ファイル / パターン | 内容 |
|---------------------|------|
| `asinsYYYY-MM-DD.csv` | 日付ごとに収集した **Amazon ASIN**（1 行 1 ASIN、`itemTweetFromTimeSale` 等が参照） |
| `asins/asins*.csv` | 同上の **アーカイブ**（2021 年頃のファイル名） |
| `titles.csv` / `titles copy.csv` | ツイート済み・候補 **商品タイトル** |
| `skipTitles.csv` | スキップしたタイトル |
| `NGtitle.csv` / `NGtitle copy.csv` | NG 判定タイトル |
| `urls.csv` | 収集 URL 一覧 |
| `mercari/mercariItemUrls*.csv` | メルカリ商品 URL のスナップショット |
| `outPutFile/.DS_Store` | システムファイル |

---

## 生成物・コミット非推奨

| パス | 説明 |
|------|------|
| `**/__pycache__/**/*.pyc` | Python 3.7 / 3.9 で生成されたキャッシュ |
| `PythonRpa/.DS_Store` | macOS |
| `geckodriver.log` | 旧 Firefox ドライバログ |

---

## ドメイン別「何のために動かすか」まとめ

| ドメイン | ビジネス目的（推定） |
|----------|---------------------|
| Amazon | アフィリエイト付きツイートで **タイムセール・自店舗商品を宣伝**。ASIN リストで二重投稿防止 |
| Twitter | **相互フォロー・せどり系コミュニティ**でのフォロワー増、宣伝アカウント運用 |
| メルカリ | 出品物の **価格チラつかせ・未売却整理・Shops 同期** |
| 楽天 e-NAVI | **ポイント獲得クリック**の自動化 |
| 東京カレンダーデート | マッチングアプリ上での **いいね・投票・スタンプ** 自動化 |

---

## 次にやるとよい整理（参考）

1. 機密を `.env` + `python-dotenv` に移し、`config.py` から読み込む  
2. パスを `Path(__file__).resolve().parent` 基準に統一（`work/rpa` → `app/rpa`）  
3. `.gitignore` に `__pycache__/`, `*.pyc`, `geckodriver.log`, `.DS_Store`, `outPutFile/*.csv`（必要ならサンプルのみ追跡）  
4. エントリースクリプトを `README` の表形式で「コマンド・目的・前提」に整理  

詳細な処理フローが必要なファイルがあれば、ファイル名を指定してもらえればそのスクリプト単位で追記できます。
