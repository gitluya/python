# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
# 去掉 "chrome正受到自动测试软件的控制" 警告框
chromeOptions = webdriver.ChromeOptions()
# chromeOptions._arguments = ['disable-infobars']
chromeOptions.add_argument('disable-infobars')
chromedriver = "C:/chromedriver.exe"# 使用指定目录下的chromedriver
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver , chrome_options=chromeOptions)

# driver = webdriver.Chrome()#谷歌
driver.maximize_window()#浏览器最大化
driver.implicitly_wait(20)
driver.get("http://data.mayi888.cn/dashboard/1")

# print (driver.get_cookies()) #打印所有cookie
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("test@mayi888.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("1q2w3e4r")
driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/form/div[4]/button").click()
# js="var q=document.body.style.zoom=0.8"#缩放至80%
# driver.execute_script(js)
# time.sleep(1)
driver.execute_script("window.open('http://data.mayi888.cn/dashboard/2')","")
handles = driver.window_handles # 获取当前所有窗口句柄
driver.switch_to.window(handles[1])
# js="var q=document.body.style.zoom=0.8"#缩放至80%
# driver.execute_script(js)
# time.sleep(1)
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg").click()
driver.find_element_by_css_selector(
    "body > span.PopoverContainer.tether-element.tether-element-attached-top.tether-target-attached-bottom.tether-target-attached-center.tether-element-attached-right.tether-enabled > span > div > div > ul > li:nth-child(2) > span:nth-child(2)").click()
driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(3) > span").click()

driver.switch_to.window(handles[0])
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg").click()
driver.find_element_by_css_selector(
    "body > span.PopoverContainer.tether-element.tether-element-attached-top.tether-target-attached-bottom.tether-target-attached-center.tether-element-attached-right.tether-enabled > span > div > div > ul > li:nth-child(2) > span:nth-child(2)").click()
driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(3) > span").click()

driver.switch_to.window(handles[1])
while True:
    # WebDriverWait(driver, 20 ,0.5).until(driver.find_element_by_css_selector("svg[name=\"expand\"]"))
    driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
    target = driver.find_element_by_css_selector(
        "#root > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(1)")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(30)

    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#到页面底部
    target = driver.find_element_by_css_selector(
        "#root > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(3)")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(30)

    target = driver.find_element_by_css_selector(
        "#root > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(5)")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(30)

    target = driver.find_element_by_css_selector(
        "#root > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(7)")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(15)

    driver.switch_to.window(handles[0])
    # WebDriverWait(driver, 20, 0.5).until(driver.find_element_by_css_selector("svg[name=\"expand\"]"))
    driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
    js="var q=document.body.style.zoom=0.8"#缩放至80%
    driver.execute_script(js)
    target = driver.find_element_by_css_selector(
        "#root > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(1)")
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(60)
    js = "var q=document.body.style.zoom=1"
    driver.execute_script(js)
    driver.switch_to.window(handles[1])
# driver.quit()