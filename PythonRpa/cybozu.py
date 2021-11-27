
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://x8zpl.cybozu.com/login")
# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_id("username-:0-text").send_keys("江端健")
driver.find_element_by_id("password-:1-text").send_keys("ebata1205")
driver.find_element_by_class_name("login-button").click()
sleep(1)
#サイボウズofficeボタンクリック
# driver.find_element_by_link_text("Cybozu Office").click()
cybozu = "/html[@class='modern region-JP js no-touch rgba cssgradients cors']/body[@class='page-index']/div[@class='container-slash']/div[@class='contents-slash clearFix-cybozu']/div[@class='contents-left-slash services-slash']/div[@class='service-list-slash']/a[@class='service-slash'][1]"
driver.find_element_by_xpath(cybozu).click()

#------------------------------------------------------------------------------------
#宛先指定された通知クリック
#------------------------------------------------------------------------------------
completeNum = 0
try:
    driver.find_element_by_class_name('vr_mentionMarkMe').click()
    sleep(1)

    for num in range(200):
        list = driver.find_elements_by_class_name('notificationSubject')
        for div in list:
            div.find_element_by_tag_name('a').click()
            try:
                driver.find_element_by_class_name('vr_hotButton').click()
                print ("宛先指定された通知1件既読完了しました。")
                completeNum += 1
            except:
                driver.find_element_by_class_name('vr_hotButton').click()
            break

        driver.back()
        driver.refresh()

    driver.back()
except:
    print ("宛先指定された通知はありませんでした。")

print ("宛先指定された通知の既読した件数："+str(completeNum)+"件"+"\n")

driver.refresh()

#------------------------------------------------------------------------------------
#未確認メッセージ
#------------------------------------------------------------------------------------
path = "/html/body/div[@id='content-wrapper']/div[@class='content']/div/table[@class='vr_topArea']/tbody/tr/td[@class='vr_topArea']/table[2]/tbody/tr/td[@id='cb7-portal-middle']/div[@id='cb7-portlet-frame-39']/div[@id='cb7-portlet-39']/div[@id='cb7-portlet-body-39']/table[@class='borderTable vr_portletBd3']/tbody/tr[1]/td[@class='vr_portletWhatsNewNotice']/table/tbody/tr/td[@class='vr_portletWhatsNew']/div[2]/a"
driver.find_element_by_xpath(path).click()

completeNum = 0
for num in range(200):
    try:
        dataList = driver.find_element_by_class_name('dataList')
    except:
        print ("未確認メッセージはありませんでした。")
        break

    alist = dataList.find_elements_by_tag_name('a')
    num = 0
    #ループは常に2回で終了
    for a in alist:
        num += 1
        if(num == 1):
            continue

        a.click()
        try:
            driver.find_element_by_class_name('vr_hotButton').click()
            print ("未確認メッセージ1件既読完了しました。")
            completeNum += 1
        except:
            driver.find_element_by_class_name('vr_hotButton').click()
        break

print ("未確認メッセージの既読した件数："+str(completeNum)+"件"+"\n")

#------------------------------------------------------------------------------------

driver.close()
exit()




# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
