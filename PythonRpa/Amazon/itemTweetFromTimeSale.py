# -*- coding: utf-8 -*-
"""
タイムセール一覧から ASIN を収集し、必要なら Twitter に投稿する。

ASIN のみ取得する場合は collect_sale_asins.py を推奨。
"""
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

import config
from env_loader import getenv, getenv_bool, load_repo_env
from BasePage import BasePage
from pages.AmazonTimeSalePage import AmazonTimeSalePage
from paths import asins_csv_for_date, ensure_output_dir
from sale_asin_collector import (
    DEALS_URL,
    append_asins_to_csv,
    collect_sale_asins_across_pages,
)

load_repo_env()

# tweepy は投稿する場合のみ
api = None
if getenv_bool("AMAZON_POST_TWEETS"):
    import tweepy

    api = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET,
    )


def _login(page: AmazonTimeSalePage, driver) -> None:
    email = getenv("AMAZON_EMAIL")
    password = getenv("AMAZON_PASSWORD")
    if not email or not password:
        print("AMAZON_EMAIL / AMAZON_PASSWORD 未設定 — ログインなしで続行")
        return
    driver.get(
        "https://www.amazon.co.jp/ap/signin?"
        "openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fgoldbox"
    )
    sleep(2)
    page.login(email, password)


def main():
    ensure_output_dir()
    today = datetime.date.today().strftime("%Y-%m-%d")
    file_path = asins_csv_for_date(today)
    if not file_path.exists():
        file_path.write_text("dummy", encoding="utf-8")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    sleep(2)

    range_count = config.timesale_watch_page_count
    amazon_page = AmazonTimeSalePage(driver)

    try:
        _login(amazon_page, driver)
        driver.get(DEALS_URL)
        sleep(3)

        dt_now = datetime.datetime.now()
        print(f"タイムセール ASIN 収集開始：{dt_now.strftime('%Y-%m-%d %H:%M:%S')}")

        records = collect_sale_asins_across_pages(
            driver, range_count, visit_deal_pages=True
        )

        dt_now = datetime.datetime.now()
        print(f"タイムセール ASIN 収集終了：{dt_now.strftime('%Y-%m-%d %H:%M:%S')} ({len(records)} 件)")

        append_asins_to_csv(file_path, [r["asin"] for r in records])
        print(f"CSV 更新: {file_path}")

        if api is None:
            print("投稿スキップ（AMAZON_POST_TWEETS=1 で tweepy 投稿を有効化）")
            return

        skip_asins = []
        skip_urls = []
        post_count = 0
        for rec in records:
            amazon_page.process_asins(
                [rec],
                skip_asins,
                skip_urls,
                BasePage,
                api,
                post_count,
                amazon_page,
                str(file_path),
            )
    finally:
        amazon_page.close()


if __name__ == "__main__":
    main()
