import datetime
import sys
from pathlib import Path

_AMAZON_DIR = Path(__file__).resolve().parent
_OUTPUT_DIR = _AMAZON_DIR.parent / "outPutFile"

# リポジトリ直下 .env を読み込む
sys.path.insert(0, str(_AMAZON_DIR.parent))
from env_loader import getenv, getenv_int, getenv_list, load_repo_env

load_repo_env()

# --- Twitter（Amazon ツイート投稿: premier_teru 系。env で上書き） ---
API_KEY = getenv("TWITTER_API_KEY")
API_SECRET = getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = getenv("TWITTER_BEARER_TOKEN")

# --- Amazon ---
affiliate_id = getenv("AMAZON_AFFILIATE_ID", "premierter0ad-22")
today = datetime.date.today()
titles_path = str(_OUTPUT_DIR / "titles.csv")
skipTitlesPath = str(_OUTPUT_DIR / "skipTitles.csv")
timesale_watch_page_count = getenv_int("AMAZON_DEALS_PAGES", 5)

# bitly（カンマ区切り。未設定なら空リスト）
access_tokens = getenv_list("BITLY_ACCESS_TOKENS")

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
    "時計",
]

stockTitles = [
    "Razer", "レイザー", "Logicool", "ロジクール", "logitech", "ELECOM", "エレコム",
    "ゲーミング", "パソコン", "キャプチャーボード", "ゼンハイザー", "モニター", "デスクトップ",
    "PC", "switch", "ゲーム", "Amazon", "アマゾン", "sony", "ソニー", "Apple",
    "アウトドア", "キャンプ", "ビール", "バーベキュー", "BBQ", "テント",
    "水着", "浮き輪", "夏", "プロテイン",
    "掃除機",
    "マスク",
    "韓国", "韓国コスメ",
]
