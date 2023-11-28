from collections import OrderedDict
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pyshorteners


class BasePage:
    
    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    @staticmethod
    def write_to_file(path, output_arr, mode='w'):
        with open(path, mode=mode) as f:
            for text in output_arr:
                f.write(str(text) + "\n")

    @staticmethod
    def deduplicate_array(arr):
        return list(OrderedDict.fromkeys(arr))

    def append_to_file(self, path, merge_arr):
        self.write_to_file(path, merge_arr, mode='a')

    @staticmethod
    def shorten_url(longUrl):
        s = pyshorteners.Shortener()
    
        # リトライロジックを実装する
        session = requests.Session()
        retry_strategy = Retry(
            total=3,  # リトライ回数を3回に設定
            backoff_factor=1,  # リトライ間隔の係数
            status_forcelist=[429, 500, 502, 503, 504],  # リトライするステータスコードを指定
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT"]  # method_whitelistをallowed_methodsに変更
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        # タイムアウト値を増やす
        timeout = 10  # タイムアウトを10秒に設定

        try:
            response = session.get(
                s.tinyurl.api_url,
                params=dict(url=longUrl),
                timeout=timeout
            )
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"エラーが発生しました: {e}")
            return None
