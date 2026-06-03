# -*- coding: utf-8 -*-
"""Amazon セール・ゴールドボックス一覧から ASIN を収集（ログイン不要）。"""
from __future__ import annotations

import re
import time
from typing import Dict, List, Optional, Set, Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from asin_utils import (
    asin_from_href,
    dedupe_asin_records,
    extract_asins_from_html,
)

# ログイン不要のメイン入口（全タイムセール一覧）
ALL_DEALS_URL = "https://www.amazon.co.jp/gp/goldbox/all-deals/?ie=UTF8&ref_=sv_whd_1"

DEALS_ENTRY_URLS = [
    ALL_DEALS_URL,
    "https://www.amazon.co.jp/deals",
    "https://www.amazon.co.jp/gp/goldbox",
]

# タイムセール検索（ページ番号を付けて巡回。クエリは削らないこと）
TIMESALE_SEARCH_URL = "https://www.amazon.co.jp/s?i=specialty-aps-sns-timesale"
TIMESALE_BROWSE_URL = "https://www.amazon.co.jp/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BB%E3%83%BC%E3%83%AB/b/"

DEFAULT_CATEGORY_SEEDS = [
    TIMESALE_SEARCH_URL,
    TIMESALE_BROWSE_URL,
]

DEALS_URL = ALL_DEALS_URL

_SKIP_CATEGORY_PATHS = (
    "/ap/",
    "/gp/help",
    "/customer-preferences",
    "/b/?",
    "register",
    "signin",
    "サービス",
    "Audible",
    "Kindle",
    "ポイント",
)

DEAL_LINK_SELECTORS = [
    '[data-testid="deal-card"] a[href]',
    '[data-testid="grid-deals-container"] a[href*="/dp/"]',
    '[data-testid="grid-deals-container"] a[href*="deal"]',
    'a[id="dealTitle"]',
    'div[class*="DealGridItem"] a[href]',
    '.DealGridItem-module__dealItemContent_1vFddcq1F8pUxM8dd9FW32 a[href]',
]

NEXT_PAGE_CLICK_SELECTORS = [
    "a.s-pagination-next:not(.s-pagination-disabled)",
    "li.a-last:not(.a-disabled) a",
    'a[aria-label="次へ"]',
    'a[aria-label="Go to next page"]',
    'a[aria-label="次のページ"]',
    ".a-pagination .a-last a",
]

# 明らかに商品ではないテキスト（紐づく ASIN を除外）
JUNK_TITLE_KEYWORDS = (
    "アマゾンマスターカード",
    "amazon mastercard",
    "プライム会員",
    "sign in",
    "ログイン",
)


def _scroll_to_load(driver: WebDriver, rounds: int = 6, pause: float = 1.0) -> int:
    """最下部までスクロール。戻り値は [data-asin] 要素数。"""
    last_count = 0
    for _ in range(rounds):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        count = len(driver.find_elements(By.CSS_SELECTOR, "[data-asin]"))
        if count == last_count and count > 0:
            break
        last_count = count
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(0.3)
    return last_count


def _wait_for_any_selector(driver: WebDriver, timeout: int = 25) -> None:
    combined = ", ".join(DEAL_LINK_SELECTORS + ["[data-asin]", 'a[href*="/dp/"]'])
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, combined))
        )
    except TimeoutException:
        print("警告: セール一覧の読み込み待ちがタイムアウトしました。取得を続行します。")


def _title_from_element(el) -> str:
    for attr in ("title", "aria-label"):
        val = el.get_attribute(attr)
        if val and val.strip():
            return val.strip()
    text = (el.text or "").strip()
    if text:
        return text
    try:
        img = el.find_element(By.TAG_NAME, "img")
        alt = img.get_attribute("alt")
        if alt:
            return alt.strip()
    except Exception:
        pass
    return ""


def _is_junk_record(rec: Dict[str, str]) -> bool:
    title = (rec.get("title") or "").lower()
    return any(k.lower() in title for k in JUNK_TITLE_KEYWORDS)


def _record_from_link(el, href: str) -> Optional[Dict[str, str]]:
    asin = asin_from_href(href)
    if not asin:
        return None
    image_url = ""
    try:
        img = el.find_element(By.TAG_NAME, "img")
        image_url = img.get_attribute("src") or ""
    except Exception:
        pass
    rec = {
        "asin": asin,
        "title": _title_from_element(el),
        "imageUrl": image_url,
        "href": href,
    }
    return None if _is_junk_record(rec) else rec


def _merge_html_asins(
    records: List[Dict[str, str]], seen_asins: Set[str], html: str
) -> int:
    added = 0
    for asin in extract_asins_from_html(html):
        if asin in seen_asins:
            continue
        seen_asins.add(asin)
        records.append({"asin": asin, "title": "", "imageUrl": "", "href": ""})
        added += 1
    return added


def collect_asins_on_current_page(driver: WebDriver) -> Tuple[List[Dict[str, str]], List[str]]:
    _scroll_to_load(driver, rounds=10, pause=0.9)
    records: List[Dict[str, str]] = []
    deal_urls: List[str] = []
    seen_asins: Set[str] = set()
    seen_urls: Set[str] = set()

    _merge_html_asins(records, seen_asins, driver.page_source)

    for el in driver.find_elements(By.CSS_SELECTOR, "[data-asin]"):
        asin = (el.get_attribute("data-asin") or "").strip().upper()
        if not re.fullmatch(r"[A-Z0-9]{10}", asin) or asin in seen_asins:
            continue
        rec = {"asin": asin, "title": _title_from_element(el), "imageUrl": "", "href": ""}
        if _is_junk_record(rec):
            continue
        seen_asins.add(asin)
        records.append(rec)

    for selector in DEAL_LINK_SELECTORS:
        for el in driver.find_elements(By.CSS_SELECTOR, selector):
            try:
                href = el.get_attribute("href") or ""
            except Exception:
                continue
            if not href or href in seen_urls:
                continue
            seen_urls.add(href)

            rec = _record_from_link(el, href)
            if rec and rec["asin"] not in seen_asins:
                seen_asins.add(rec["asin"])
                records.append(rec)
            elif not rec and any(
                token in href for token in ("/deal/", "/promotions/", "/promotion/")
            ):
                if href not in deal_urls:
                    deal_urls.append(href)

    for el in driver.find_elements(By.CSS_SELECTOR, 'a[href*="/dp/"]'):
        try:
            href = el.get_attribute("href") or ""
        except Exception:
            continue
        if not href or href in seen_urls:
            continue
        seen_urls.add(href)
        rec = _record_from_link(el, href)
        if rec and rec["asin"] not in seen_asins:
            seen_asins.add(rec["asin"])
            records.append(rec)

    _merge_html_asins(records, seen_asins, driver.page_source)

    return dedupe_asin_records(records), deal_urls


def collect_asins_from_deal_landing(driver: WebDriver, url: str) -> List[Dict[str, str]]:
    if "/dp/" in url:
        asin = asin_from_href(url)
        if not asin:
            return []
        rec = {"asin": asin, "title": "", "imageUrl": "", "href": url}
        return [] if _is_junk_record(rec) else [rec]

    driver.get(url)
    time.sleep(2)
    records, _ = collect_asins_on_current_page(driver)
    return [r for r in records if not _is_junk_record(r)]


def _count_listing_asins(driver: WebDriver) -> int:
    dom = {
        (el.get_attribute("data-asin") or "").strip().upper()
        for el in driver.find_elements(By.CSS_SELECTOR, "[data-asin]")
        if re.fullmatch(r"[A-Z0-9]{10}", (el.get_attribute("data-asin") or "").strip())
    }
    return len(dom | extract_asins_from_html(driver.page_source))


def _pagination_hrefs(driver: WebDriver) -> List[str]:
    """ページネーション strip から未訪問っぽい URL を収集。"""
    hrefs: List[str] = []
    seen: Set[str] = set()
    for el in driver.find_elements(
        By.CSS_SELECTOR,
        ".s-pagination-item, .a-pagination a, a.s-pagination-button",
    ):
        try:
            href = el.get_attribute("href") or ""
            text = (el.text or "").strip()
        except Exception:
            continue
        if not href or href in seen:
            continue
        if "javascript:" in href:
            continue
        # 数字ページ or next
        if text.isdigit() or el.get_attribute("aria-label") in (
            "Go to next page",
            "次へ",
            "次のページ",
        ):
            seen.add(href)
            hrefs.append(href)
    return hrefs


def go_to_next_listing_page(driver: WebDriver) -> bool:
    """
    次の一覧へ進む。クリック → 失敗時はページネーション URL 直遷移 → スクロール増分。
    """
    before_url = driver.current_url
    before_count = _count_listing_asins(driver)

    for sel in NEXT_PAGE_CLICK_SELECTORS:
        for el in driver.find_elements(By.CSS_SELECTOR, sel):
            try:
                if not el.is_displayed():
                    continue
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                time.sleep(0.3)
                el.click()
                time.sleep(3)
                _wait_for_any_selector(driver, timeout=15)
                if (
                    driver.current_url != before_url
                    or _count_listing_asins(driver) > before_count
                ):
                    print(f"  次ページ（クリック）: {driver.current_url[:90]}…")
                    return True
            except Exception:
                continue

    for href in _pagination_hrefs(driver):
        if href == before_url:
            continue
        try:
            driver.get(href)
            time.sleep(3)
            _wait_for_any_selector(driver, timeout=15)
            if _count_listing_asins(driver) > 0:
                print(f"  次ページ（URL）: {href[:90]}…")
                return True
        except Exception:
            continue

    _scroll_to_load(driver, rounds=4, pause=1.2)
    after_count = _count_listing_asins(driver)
    if after_count > before_count:
        print(f"  追加読み込み（スクロール）: {before_count} → {after_count} 件")
        return True

    return False


def discover_category_urls(driver: WebDriver) -> List[str]:
    """all-deals から「タイムセール」系リンクだけ拾う（汎用 /b/ は除外）。"""
    found: List[str] = []
    seen: Set[str] = set()
    keywords = ("タイムセール", "timesale", "goldbox", "deal", "セール")

    for el in driver.find_elements(By.CSS_SELECTOR, "a[href]"):
        try:
            href = (el.get_attribute("href") or "").split("#")[0]
            text = (el.text or "").strip()
        except Exception:
            continue
        if "amazon.co.jp" not in href:
            continue
        hay = f"{href} {text}".lower()
        if not any(k in hay for k in keywords):
            continue
        if "/dp/" in href:
            continue
        if any(skip in href for skip in _SKIP_CATEGORY_PATHS):
            continue
        key = _seed_dedupe_key(href)
        if key in seen:
            continue
        seen.add(key)
        found.append(key)
    return found


def _seed_dedupe_key(url: str) -> str:
    return url.split("#")[0].strip()


def _is_valid_seed(url: str) -> bool:
    u = _seed_dedupe_key(url)
    if u in ("https://www.amazon.co.jp", "https://www.amazon.co.jp/"):
        return False
    if u.endswith("/s") or u.endswith("/b"):
        return False
    return "amazon.co.jp" in u


def _search_page_url(base: str, page: int) -> str:
    if page <= 1:
        return base
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}page={page}"


def _crawl_search_listing(
    driver: WebDriver,
    base_url: str,
    seen_asins: Set[str],
    all_records: List[Dict[str, str]],
    all_deal_urls: List[str],
    *,
    page_count: int,
    max_pages_per_seed: int,
    visited_page_urls: Set[str],
) -> None:
    """検索結果（s?i=timesale 等）を page=1,2,3… で巡回。"""
    print(f"\n--- 検索巡回: {base_url[:100]}")
    unlimited = page_count <= 0
    page_index = 0
    stale_pages = 0

    while True:
        page_index += 1
        if page_index > max_pages_per_seed:
            print(f"  ページ上限（{max_pages_per_seed}）")
            break

        url = _search_page_url(base_url, page_index)
        if url in visited_page_urls:
            print("  既訪問 URL")
            break
        visited_page_urls.add(url)

        driver.get(url)
        time.sleep(2)
        try:
            WebDriverWait(driver, 18).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "[data-asin], .s-result-item, .sg-col-inner")
                )
            )
        except TimeoutException:
            html_n = len(extract_asins_from_html(driver.page_source))
            if html_n == 0:
                print(f"  ページ {page_index}: 検索結果なし（終了）")
                break
            print(f"  ページ {page_index}: DOM 待ちタイムアウト（HTML から {html_n} 件）")

        records, deal_urls = collect_asins_on_current_page(driver)
        added = _append_records(all_records, seen_asins, records)
        for du in deal_urls:
            if du not in all_deal_urls:
                all_deal_urls.append(du)

        print(
            f"  検索 page={page_index}: +{added} 件"
            f"（累計 {len(seen_asins)}）"
        )

        if not unlimited and page_index >= page_count:
            break

        if added == 0:
            stale_pages += 1
            if stale_pages >= 2:
                print("  連続で新規なしのため終了")
                break
        else:
            stale_pages = 0

        if not go_to_next_listing_page(driver):
            continue


def _append_records(
    all_records: List[Dict[str, str]],
    seen_asins: Set[str],
    records: List[Dict[str, str]],
) -> int:
    added = 0
    for rec in records:
        if _is_junk_record(rec):
            continue
        asin = rec["asin"]
        if asin in seen_asins:
            continue
        seen_asins.add(asin)
        all_records.append(rec)
        added += 1
    return added


def _crawl_listing_url(
    driver: WebDriver,
    url: str,
    seen_asins: Set[str],
    all_records: List[Dict[str, str]],
    all_deal_urls: List[str],
    *,
    page_count: int,
    max_pages_per_seed: int,
    visited_page_urls: Set[str],
) -> None:
    """1 つの一覧 URL をページ送りしながら ASIN を集める。"""
    print(f"\n--- 巡回: {url[:100]}")
    if "?" in url and ("s?" in url or "i=" in url):
        _crawl_search_listing(
            driver,
            url,
            seen_asins,
            all_records,
            all_deal_urls,
            page_count=page_count,
            max_pages_per_seed=max_pages_per_seed,
            visited_page_urls=visited_page_urls,
        )
        return

    try:
        driver.get(url)
        time.sleep(2.5)
        _wait_for_any_selector(driver, timeout=10)
    except Exception as e:
        print(f"  開けませんでした: {e}")
        return

    unlimited = page_count <= 0
    page_index = 0

    while True:
        page_index += 1
        if page_index > max_pages_per_seed:
            print(f"  シードあたり上限（{max_pages_per_seed} ページ）で次へ")
            break

        cur = driver.current_url.split("#")[0]
        if cur in visited_page_urls and page_index > 1:
            print("  既訪問 URL のため終了")
            break
        visited_page_urls.add(cur)

        records, deal_urls = collect_asins_on_current_page(driver)
        added = _append_records(all_records, seen_asins, records)
        for du in deal_urls:
            if du not in all_deal_urls:
                all_deal_urls.append(du)

        print(
            f"  ページ {page_index}: +{added} 件"
            f"（累計 {len(seen_asins)} / 画面内 {len(records)}）"
        )

        if not unlimited and page_index >= page_count:
            break

        before_total = len(seen_asins)
        if not go_to_next_listing_page(driver):
            # スクロールだけで増えるか最終確認
            _scroll_to_load(driver, rounds=6)
            records2, _ = collect_asins_on_current_page(driver)
            added2 = _append_records(all_records, seen_asins, records2)
            if added2:
                print(f"  スクロール追加分: +{added2}")
            if len(seen_asins) == before_total and added2 == 0:
                print("  次ページなし")
                break
            if len(seen_asins) == before_total:
                break
            continue

        if len(seen_asins) == before_total:
            print("  新規 ASIN なしのためこのシードを終了")
            break


def collect_sale_asins_across_pages(
    driver: WebDriver,
    page_count: int,
    *,
    visit_deal_pages: bool = True,
    max_steps: int = 80,
    extra_seed_urls: Optional[List[str]] = None,
    max_pages_per_seed: int = 40,
) -> List[Dict[str, str]]:
    """
    ログインなしでセール ASIN を可能な限り収集。

    - gp/goldbox/all-deals（全タイムセール）
    - ページ内のカテゴリ /b/ リンク
    - DEFAULT_CATEGORY_SEEDS / .env の AMAZON_SALE_SEED_URLS

    page_count <= 0 のとき各シードで次ページがなくなるまで巡回。
    """
    all_records: List[Dict[str, str]] = []
    all_deal_urls: List[str] = []
    seen_asins: Set[str] = set()
    visited_page_urls: Set[str] = set()

    driver.get(ALL_DEALS_URL)
    time.sleep(3)
    _wait_for_any_selector(driver, timeout=25)

    seeds: List[str] = [ALL_DEALS_URL, TIMESALE_SEARCH_URL, TIMESALE_BROWSE_URL]
    seeds.extend(discover_category_urls(driver))
    seeds.extend(DEFAULT_CATEGORY_SEEDS)
    if extra_seed_urls:
        seeds.extend(extra_seed_urls)

    unique_seeds: List[str] = []
    seen_seeds: Set[str] = set()
    for s in seeds:
        if not _is_valid_seed(s):
            continue
        key = _seed_dedupe_key(s)
        if key in seen_seeds:
            continue
        seen_seeds.add(key)
        unique_seeds.append(key)

    print(f"巡回シード数: {len(unique_seeds)}（ログインなし）")
    for i, s in enumerate(unique_seeds, 1):
        print(f"  {i}. {s[:95]}")

    seed_count = 0
    for seed in unique_seeds:
        seed_count += 1
        if seed_count > max_steps:
            print(f"シード上限（{max_steps}）に達しました。")
            break
        if "s?" in seed or ("/s?" in seed) or ("i=" in seed and "/s" in seed):
            _crawl_search_listing(
                driver,
                seed,
                seen_asins,
                all_records,
                all_deal_urls,
                page_count=page_count,
                max_pages_per_seed=max_pages_per_seed,
                visited_page_urls=visited_page_urls,
            )
        else:
            _crawl_listing_url(
                driver,
                seed,
                seen_asins,
                all_records,
                all_deal_urls,
                page_count=page_count,
                max_pages_per_seed=max_pages_per_seed,
                visited_page_urls=visited_page_urls,
            )

    if visit_deal_pages and all_deal_urls:
        print(f"\nセール詳細 URL {len(all_deal_urls)} 件を追加収集…")
        for i, url in enumerate(all_deal_urls[:50], 1):
            try:
                extra = collect_asins_from_deal_landing(driver, url)
                added = _append_records(all_records, seen_asins, extra)
                if added:
                    print(f"  [{i}] +{added}")
            except Exception as e:
                print(f"  [{i}] スキップ: {e}")

    print(f"\n合計 {len(all_records)} ASIN（ユニーク）")
    return dedupe_asin_records(all_records)


def load_existing_asins_csv(path) -> Set[str]:
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    return {
        a.strip().upper()
        for a in text.replace("\n", ",").split(",")
        if a.strip() and a.strip().lower() != "dummy"
    }


def append_asins_to_csv(path, asins: List[str], existing: Optional[Set[str]] = None) -> int:
    known = existing or load_existing_asins_csv(path)
    added = 0
    with path.open("a", encoding="utf-8") as f:
        for asin in asins:
            asin = asin.upper()
            if asin in known:
                continue
            f.write(f",{asin}")
            known.add(asin)
            added += 1
    return added


def save_asin_report(path, records: List[Dict[str, str]]) -> None:
    lines = ["asin\ttitle"]
    for rec in records:
        title = (rec.get("title") or "").replace("\t", " ").replace("\n", " ")
        lines.append(f"{rec['asin']}\t{title}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
