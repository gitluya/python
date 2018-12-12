# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
# driver = webdriver.Firefox()#火狐
# driver = webdriver.Ie()#IE
# driver = webdriver.Chrome()#谷歌
# 去掉 "chrome正受到自动测试软件的控制" 警告框
chromeOptions = webdriver.ChromeOptions()
# chromeOptions._arguments = ['disable-infobars']
chromeOptions.add_argument('disable-infobars')
chromedriver = "C:/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver , chrome_options=chromeOptions)
# driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.maximize_window()
driver.get("http://www.baidu.com")
js="var q=document.body.style.zoom=0.8"
driver.execute_script(js)

# driver.execute_script("window.open('http://news.baidu.com/')","")
# handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
# driver.switch_to.window(handles[0])
driver.find_element_by_id("kw").send_keys("Selenium")
js="var q=document.body.style.zoom=1"
driver.execute_script(js)
driver.find_element_by_id("su").click()
time.sleep(3)
# # js="var q=document.documentElement.scrollTop=10000"
# # driver.execute_script(js)
driver.quit()