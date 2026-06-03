import sys
from pathlib import Path

_AMAZON_ROOT = Path(__file__).resolve().parents[1]
if str(_AMAZON_ROOT) not in sys.path:
    sys.path.insert(0, str(_AMAZON_ROOT))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePage import BasePage
from time import sleep
import datetime
import config
from asin_utils import asin_from_href
from sale_asin_collector import (
    collect_asins_from_deal_landing,
    collect_asins_on_current_page,
    paginate_deals_list,
)


class AmazonTimeSalePage(BasePage):

    def __init__(self, driver):
        # url = "https://www.amazon.co.jp/deal/7f92b4ad/ref=gbps_rlm_m-8_da49_7f92b4ad?showVariations=true&smid=AN1VRQENFRJN5&pf_rd_p=dc07c715-6714-4621-8dce-d8aeabd7da49&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=5118913051&pf_rd_m=AN1VRQENFRJN5&pf_rd_r=ZVP07VP0HW76DXQBQR0S"
        url = "https://www.amazon.co.jp/blackfriday"
        super().__init__(driver=driver, url=url)

    def login(self, loginId, passWord):
        search = self.driver.find_element(By.NAME, 'email')
        search.send_keys(loginId)
        search.send_keys(Keys.ENTER)
        search = self.driver.find_element(By.NAME, 'password')
        search.send_keys(passWord)
        search.send_keys(Keys.ENTER)
        # sleep(40)
        sleep(10)
        print("login!!!")

    def get_class_named_elements_from_product_list(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)

    def get_multiple_dom_from_product_list_by_classname(self, classNames):
        return self.driver.find_elements(By.CSS_SELECTOR, classNames)

    def get_dom_from_product_list_by_tagname(self, tagName):
        return self.driver.find_elements(By.TAG_NAME, tagName)

    def open_product_page_directly_by_url(self, url):
        self.driver.get(url)

    def open_next_page(self):
        aLasts = self.driver.find_elements(By.CLASS_NAME, "a-last")
        for aLast in aLasts:
            try:
                aLast.find_element(By.TAG_NAME, "a").click()
                break
            except:
                continue
        sleep(5)

    def wait_check(self):
        now = datetime.datetime.now()
        if (7 <= now.hour <= 9) or (11 <= now.hour <= 14) or (17 <= now.hour <= 23):
            print("通勤/ランチ/帰宅中・帰宅後")
        else:
            diff_hours = 7 - now.hour
            if diff_hours <= 0:
                diff_hours += 24
            print(f"今{now.hour}時\n{diff_hours}時間後投稿開始")
            sleep(diff_hours * 3600)

    def wait_for_three_hrs_for_300_posts(self):
        intervals = [30, 60, 90, 120, 150]
        for interval in intervals:
            print(f"{interval}分休憩🍵経過...")
            sleep(interval * 60)
        print("3時間休憩🍵終了！")

    def wait_for_24_hrs(self):
        total_minutes = 1440  # 24時間を分で表したもの
        interval = 15  # 休憩間隔（15分）
        total_elapsed = 0  # 経過時間の合計

        while total_elapsed < total_minutes:
            print(f"合計{total_elapsed}分休憩🍵経過...")
            sleep(interval * 60)  # 15分休憩
            total_elapsed += interval  # 経過時間を更新

        print("24時間休憩🍵終了！")

    def extract_asin_info(self, item_tag):
        href = item_tag.get_attribute("href") or ""
        asin = asin_from_href(href)
        if not asin:
            return None
        image_url = ""
        title = item_tag.get_attribute("title") or ""
        try:
            image_url = item_tag.find_element(By.TAG_NAME, "img").get_attribute("src") or ""
        except Exception:
            pass
        return {"asin": asin, "title": title, "imageUrl": image_url}

    def collect_asins(self, url, atag_asins=None):
        asins = list(atag_asins or [])
        dt_now = datetime.datetime.now()
        print(f"ASIN収集開始：{dt_now.strftime('%Y-%m-%d %H:%M:%S')} url={url[:80]}")

        try:
            extra = collect_asins_from_deal_landing(self.driver, url)
            for rec in extra:
                if not any(a["asin"] == rec["asin"] for a in asins):
                    asins.append(rec)
                    print(f'{rec["asin"]}：{rec.get("title", "")}')
        except Exception as e:
            print(f"セール詳細の取得に失敗: {e}")

        dt_now = datetime.datetime.now()
        print(f"ASIN収集終了：{dt_now.strftime('%Y-%m-%d %H:%M:%S')} ({len(asins)} 件)")
        return asins

    def clean_title(self, title, splits):
        for split in splits:
            if split in title:
                title = title.replace(split, ' ')
        return title

    def should_skip_asin(self, asin, skip_titles, skip_asins):
        for skip_title in skip_titles:
            if skip_title in asin["title"]:
                return True
        return asin["asin"] in skip_asins

    def process_asins(
            self, asins, skipAsins, skipUrls,
            BasePage, api, postCount, amazonPage, filePath):
        notTitleCount = 0
        splits = ['〃', '仝', 'ゝ', 'ゞ', '々', '〆', 'ヾ', '―', '‐', '／', '〇', 'ヽ', '＿', '￣', '¨', '｀', '´', '゜', '゛', '＼', '§', '＾', '≫', '￢', '⇒', '⇔', '∀', '∃', '∠', '⊥', '⌒', '∂', '∇', '≡', '∨', '≪', '†', '√', '∽', '∝', '∵', '∫', '∬', 'Å', '‰', '♯',
                    '♭', '♪', '‡', '～', '′', '≒', '×', '∥', '∧', '｜', '…', '±', '÷', '≠', '≦', '≧', '∞', '∴', '♂', '♀', '∪', '‥', '°', '⊃', '⊂', '⊇', '∩', '⊆', '∋', '∈', '〓', '〒', '※', '″', '☆', '★', ',', '.', ';', "'", '"', '?', '!', '(', ')', '（', '）', '/', '【', '】', '[', ']','「','」']

        for asin in asins:
            titleSplit = asin["title"]
            titleSplit = self.clean_title(titleSplit, splits)

            with open(config.titles_path, mode='a') as f:
                ts = str(",".join(list(set(titleSplit.split()))))
                f.write(ts)

            if self.should_skip_asin(asin, config.skip_titles, skipAsins):
                print("投稿済みのASINのためスキップしました。")
                continue
            
            longUrl = f"https://www.amazon.co.jp/gp/product/{asin['asin']}/ref=as_li_qf_asin_il_tl?ie=UTF8&tag={config.affiliate_id}&creative=1211&linkCode=as2&creativeASIN={asin['asin']}"
            createUrl = BasePage.shorten_url(longUrl)

            if not asin["title"]:
                notTitleCount += 1
                print(f"タイトルがうまく取得できていないためハッシュタグとサムネURLだけ投稿します{notTitleCount}")

            title = asin["title"]
            # categorys = ["Amazon", "タイムセール", "Amazonタイムセール"]
            # categorys = ["Amazon", "タイムセール", "Amazonタイムセール祭り"]
            categorys = ["Amazon", "タイムセール", "Amazonブラックフライデー"]
            hashtags = "\n#" + ' #'.join(categorys)
            minusCount = len(hashtags)

            if len(title) > 140 - minusCount:
                title = title[:-(len(title) - 140) - minusCount]
            updatePost = title + hashtags

            # if postCount > 0 and postCount % 300 == 0:
            if postCount > 0 and postCount % 50 == 0:
                amazonPage.wait_for_24_hrs()
            try:
                if createUrl in skipUrls:
                    print("新しい短縮URLが取得できない為、終了します。")
                    exit()

                # amazonPage.wait_check()
                api.create_tweet(text=f"{updatePost}\n{createUrl}")
                skipUrls.append(createUrl)
                postCount += 1
                dt_now = datetime.datetime.now()
                print("投稿成功しました！")
            except Exception as e:
                print(e)
                print("ーーーーーーーーーーーーーーー")
                if "User is over daily status update limit" in str(e):
                    amazonPage.wait_for_24_hrs()
                    postCount = 0
                elif "duplicate" in str(e):
                    print("重複した投稿内容です")

            dt_now = datetime.datetime.now()
            postDateTime = dt_now.strftime('%Y-%m-%d %H:%M:%S')
            print("ーーーーーーーーーーーーーーー")
            print(f"投稿時間： {postDateTime}")
            print(f"商品名： {asin['title']}")
            print(f"ASIN： {asin['asin']}")
            print("ーーーーーーーーーーーーーーー")

            if asin["title"] not in config.skip_titles:
                with open(filePath, mode='a') as f:
                    f.write(f",{asin['asin']}")

                with open(filePath) as f:
                    oldAsins = f.read()
                    skipAsins = list(set(oldAsins.split(',')))

    def process_range_count(self, amazon_page, range_count, skip_atags_asins):
        """一覧を range_count ページ分走査し、deal URL と一覧上の ASIN を返す。"""
        all_urls = []
        listing_asins = []

        for num in range(range_count):
            print(f"{num + 1}/{range_count} ページ目")
            records, deal_urls = collect_asins_on_current_page(self.driver)

            for rec in records:
                if rec["asin"] not in skip_atags_asins:
                    skip_atags_asins.append(rec["asin"])
                    listing_asins.append(rec)
                    print(f"{rec['asin']}：{rec.get('title', '')}")

            for url in deal_urls:
                if url not in all_urls:
                    all_urls.append(url)
                    print(url)

            if num < range_count - 1:
                if not paginate_deals_list(self.driver):
                    print("次ページなし")
                    break

        return all_urls, listing_asins
