#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amazon セール（ログイン不要）から ASIN をすべて収集する。

使い方:
  cd PythonRpa/Amazon
  python3 collect_sale_asins.py          # .env の AMAZON_DEALS_PAGES（0=全ページ）
  python3 collect_sale_asins.py --all    # 明示的に全ページ＋セール詳細も深掘り

環境変数:
  AMAZON_SKIP_LOGIN=1 … 既定推奨（ログインしない）
  AMAZON_DEALS_PAGES=0 … 0 で全ページ巡回
"""
from __future__ import annotations

import argparse
import datetime
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config
from env_loader import getenv, getenv_bool, getenv_int, getenv_list, load_repo_env
from paths import asins_csv_for_date, ensure_output_dir
from sale_asin_collector import (
    DEALS_URL,
    append_asins_to_csv,
    collect_sale_asins_across_pages,
    save_asin_report,
)

load_repo_env()


def build_driver(headless: bool) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--lang=ja-JP")
    options.add_argument("--window-size=1280,900")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def main() -> int:
    parser = argparse.ArgumentParser(description="Amazon セール ASIN 収集")
    parser.add_argument(
        "--all",
        action="store_true",
        help="全ページ＋セール詳細 URL まで収集（AMAZON_DEALS_PAGES=0 と同義）",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=None,
        help="巡回する一覧ページ数（0 または省略時は .env / --all で全件）",
    )
    parser.add_argument("--headless", action="store_true", help="ヘッドレス Chrome")
    parser.add_argument(
        "--no-deal-pages",
        action="store_true",
        help="セール詳細 URL への深掘りをしない",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="asins{date}.tsv に asin と title も出力",
    )
    args = parser.parse_args()

    ensure_output_dir()
    today = datetime.date.today().strftime("%Y-%m-%d")
    csv_path = asins_csv_for_date(today)
    if not csv_path.exists():
        csv_path.write_text("dummy", encoding="utf-8")

    if getenv_bool("CHROME_HEADLESS"):
        args.headless = True

    if args.pages is None:
        pages = 0 if (args.all or getenv_bool("AMAZON_DEALS_ALL")) else getenv_int(
            "AMAZON_DEALS_PAGES", 0
        )
    else:
        pages = 0 if args.all else args.pages

    skip_login = getenv_bool("AMAZON_SKIP_LOGIN", default=True)
    if not skip_login:
        print("警告: AMAZON_SKIP_LOGIN=0 ですが、このスクリプトはログイン処理を行いません。")

    driver = build_driver(args.headless)
    started = datetime.datetime.now()
    print(f"開始: {started.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"出力: {csv_path}")
    print(f"モード: ログインなし / ページ={'全件' if pages <= 0 else pages}")

    try:
        records = collect_sale_asins_across_pages(
            driver,
            pages,
            visit_deal_pages=not args.no_deal_pages,
            extra_seed_urls=getenv_list("AMAZON_SALE_SEED_URLS"),
            max_pages_per_seed=getenv_int("AMAZON_MAX_PAGES_PER_SEED", 40),
            max_steps=getenv_int("AMAZON_MAX_SEEDS", 80),
        )

        asin_list = [r["asin"] for r in records]
        added = append_asins_to_csv(csv_path, asin_list)
        print(f"収集 ASIN 数: {len(records)}（CSV 新規追記: {added}）")

        if args.report:
            report_path = csv_path.with_suffix(".tsv")
            save_asin_report(report_path, records)
            print(f"レポート: {report_path}")

        for rec in records[:20]:
            title = (rec.get("title") or "")[:60]
            print(f"  {rec['asin']}  {title}")
        if len(records) > 20:
            print(f"  … 他 {len(records) - 20} 件")

        if not records:
            print(
                "ASIN が 0 件でした。セレクタ変更・ログイン必要・CAPTCHA の可能性があります。",
                file=sys.stderr,
            )
            return 1
        return 0
    finally:
        driver.quit()
        ended = datetime.datetime.now()
        print(f"終了: {ended.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    sys.exit(main())
