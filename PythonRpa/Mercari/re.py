from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

userdata_dir = '/private/var/folders/qj/lgc5qm9n6f18dp7h960p0csc0000gn/T/.com.google.Chrome.Ll9fxb'
os.makedirs(userdata_dir, exist_ok=True)
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + userdata_dir)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("***********")


# options = webdriver.chrome.options.Options()
# profile_path = '/private/var/folders/qj/lgc5qm9n6f18dp7h960p0csc0000gn/T/.com.google.Chrome.Ll9fxb'
# options.add_argument('--user-data-dir=' + profile_path)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver.get("********")