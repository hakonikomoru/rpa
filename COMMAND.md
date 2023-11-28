https://kurozumi.github.io/selenium-python/locating-elements.html
pythonselenium用HTML取得関数

```
# get_attribute("取りたい属性")
# find_element_by_id()
# find_element_by_name()
# find_element_by_xpath()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_tag_name()
# find_element_by_class_name()
# find_element_by_css_selector()

# find_elements_by_name()
# find_elements_by_xpath()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_tag_name()
# find_elements_by_class_name()
# find_elements_by_css_selector()

# 古いメソッド	新しいメソッド
# find_element_by_id(id)	find_element(By.ID, id)
# find_element_by_name(name)	find_element(By.NAME, name)
# find_element_by_xpath(xpath)	find_element(By.XPATH, xpath)
# find_element_by_link_text(text)	find_element(By.LINK_TEXT, text)
# find_element_by_partial_link_text(text)	find_element(By.PARTIAL_LINK_TEXT, text)
# find_element_by_tag_name(name)	find_element(By.TAG_NAME, name)
# find_element_by_class_name(name)	find_element(By.CLASS_NAME, name)
# find_element_by_css_selector(css_selector)	find_element(By.CSS_SELECTOR, css_selector)

# 古いメソッド	新しいメソッド
# find_elements_by_name(name)	find_elements(By.NAME, name)
# find_elements_by_xpath(xpath)	find_elements(By.XPATH, xpath)
# find_elements_by_link_text(text)	find_elements(By.LINK_TEXT, text)
# find_elements_by_partial_link_text(text)	find_elements(By.PARTIAL_LINK_TEXT, text)
# find_elements_by_tag_name(name)	find_elements(By.TAG_NAME, name)
# find_elements_by_class_name(name)	find_elements(By.CLASS_NAME, name)
# find_elements_by_css_selector(css_selector)	find_elements(By.CSS_SELECTOR, css_selector)

# スクロール最上
# execute_script('window.scroll(0,0)')
# クロール最下
# execute_script('window.scroll(0,1000000)')
```