from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# headless-chromeの立ち上げ　
options = Options()
options.add_argument('--headless')
executable_path="/usr/local/bin/chromedriver"
service_args=["--verbose", "--log-path=/content/chromedriver.log"]

driver = webdriver.Chrome(chrome_options=options, executable_path=executable_path, service_args=service_args)

# Googleのトップ画面を開く
driver.get('https://www.google.co.jp/')
print(driver.page_source)
