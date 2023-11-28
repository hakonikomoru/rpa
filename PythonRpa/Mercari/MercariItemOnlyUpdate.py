# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages import MercariShopsPage
from webdriver_manager.chrome import ChromeDriverManager
import datetime

# プロファイル作成
# userdata_dir = '/private/var/folders/qj/lgc5qm9n6f18dp7h960p0csc0000gn/T/.com.google.Chrome.Ll9fxb'
# os.makedirs(userdata_dir, exist_ok=True)
# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=' + userdata_dir)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# reCAPTCHA突破
# options = webdriver.chrome.options.Options()
# profile_path = '/private/var/folders/qj/lgc5qm9n6f18dp7h960p0csc0000gn/T/.com.google.Chrome.Ll9fxb'
# options.add_argument('--user-data-dir=' + profile_path)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
mercariShopsPage = MercariShopsPage(driver)
mercariShopsPage.open()
# mercariShopsPage.login('ebatajunko0228@gmail.com', 'Kensyo01')
# sleep(90)


# 商品URL取得
mercariShopsPage.open_product_page_directly_by_url('https://mercari-shops.com/shops/3uFoNvuTKzdVWB8MRC72dQ')
itemDivs = mercariShopsPage.get_class_named_elements_from_product_list("css-m3mjtg")
mercariShopsPage.scroll_to_bottom(20)
mercariShopsPage.scroll_to_top()

urls = []
for itemDiv in itemDivs:
    dt_now = datetime.datetime.now()
    urls.append(itemDiv.find_element(By.TAG_NAME, 'a').get_attribute("href")+'_for_seller')
    # print(itemDiv.find_element(By.TAG_NAME, 'img').get_attribute("src"))

mercariShopsPage.write_output_to_file('/Users/ebata/work/rpa/PythonRpa/outPutFile/mercari/mercariItemUrls'+str(dt_now.strftime('%Y-%m-%d %H-%M'))+'.csv', urls)

# loginは1分くらいで処理を終了させる

# 商品管理の画面を開く
# https://mercari-shops.com/seller/shops
# ここで「ショップページを確認する」buttonを押下する
# その前の画面
# https://mercari-shops.com/shops/3uFoNvuTKzdVWB8MRC72dQ
# その前の画面
# https://mercari-shops.com/products/NVRHo2e5yfQMamiDYvvA53?source=shop_page_for_seller
# 編集画面
# https://mercari-shops.com/seller/shops/3uFoNvuTKzdVWB8MRC72dQ/products/NVRHo2e5yfQMamiDYvvA53/edit
# mercariShopsPage.open_product_page_directly_by_url('https://mercari-shops.com/seller/shops/3uFoNvuTKzdVWB8MRC72dQ/products')
# print('商品管理の画面へ遷移')

# itemsButtons = mercariShopsPage.get_class_named_elements_from_product_list("css-155za0w")
# for button in itemsButtons:
#     button.click()
#     sleep(5)
#     mercariShopsPage.transition_to_edit_screen('/edit')
#     buttons = mercariShopsPage.get_one_dom_from_product_list_by_classname('css-5k21z4')
#     buttons.find_elements(By.TAG_NAME, 'button')[0].click()
#     sleep(5)
#     mercariShopsPage.open_product_page_directly_by_url('https://mercari-shops.com/seller/shops/3uFoNvuTKzdVWB8MRC72dQ/products')