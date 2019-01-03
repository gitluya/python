# -*- coding: utf-8 -*-
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
import actions as actions
from selenium import webdriver
# driver = webdriver.Firefox()#火狐
# driver = webdriver.Ie()#IE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
# # 去掉 "chrome正受到自动测试软件的控制" 警告框
# chromeOptions = webdriver.ChromeOptions()
# # chromeOptions._arguments = ['disable-infobars']
# chromeOptions.add_argument('disable-infobars')
# driver = webdriver.Chrome(chrome_options=chromeOptions)

# driver = webdriver.Chrome()#谷歌(只用这一句的话，用的好像是python安装目录下的chromedriver)
# 使用指定目录下的chromedriver（？环境变量PATH中没配置也可以）
# chromedriver = "C:/Users/yaya/AppData/Local/Google/Chrome/Application/chromedriver.exe"
chromedriver = "C:/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
 ## 创建浏览器对象
driver = webdriver.Chrome(chromedriver)

driver.maximize_window()
driver.get("http://www.baidu.com")

# driver.find_element_by_id("su").click()
driver.quit()