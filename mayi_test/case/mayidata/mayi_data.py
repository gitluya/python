# -*- coding: utf-8 -*-
import time
from telnetlib import EC

from selenium import webdriver
# driver = webdriver.Firefox()#火狐
# driver = webdriver.Ie()#IE
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 去掉 "chrome正受到自动测试软件的控制" 警告框
chromeOptions = webdriver.ChromeOptions()
chromeOptions._arguments = ['disable-infobars']
driver = webdriver.Chrome(chrome_options=chromeOptions)

# driver = webdriver.Chrome()#谷歌
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://data.mayi888.cn/dashboard/1")
# print (driver.get_cookies()) #打印所有cookie
# 添加Cookie
# cookie_1 = {'domain': '.mayi888.cn', 'expiry': 1542132461, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2076402420.1542046062'}
# cookie_2 = {'domain': '.mayi888.cn', 'expiry': 1605118061, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.398077250.1542046062'}
# driver.add_cookie(cookie_1)
# driver.add_cookie(cookie_2)
# driver.refresh()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("test@mayi888.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("1q2w3e4r")
driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/form/div[4]/button").click()
print("登录")
'''
try:
    element = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg"))
    )
    # EC.presence_of_element_located
finally:
    driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg").click()
    driver.find_element_by_css_selector(
    "body > span.PopoverContainer.tether-element.tether-element-attached-top.tether-target-attached-bottom.tether-target-attached-center.tether-element-attached-right.tether-enabled > span > div > div > ul > li:nth-child(2) > span:nth-child(2)").click()
'''
# print (driver.get_cookies()) #打印所有cookie
# driver.execute_script("window.open('http://data.mayi888.cn/dashboard/2#refresh=60')","")
driver.execute_script("window.open('http://data.mayi888.cn/dashboard/2')","")
handles = driver.window_handles # 获取当前所有窗口句柄
driver.switch_to.window(handles[1])
# ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg").click()
driver.find_element_by_css_selector(
    "body > span.PopoverContainer.tether-element.tether-element-attached-top.tether-target-attached-bottom.tether-target-attached-center.tether-element-attached-right.tether-enabled > span > div > div > ul > li:nth-child(2) > span:nth-child(2)").click()
driver.switch_to.window(handles[0])
driver.find_element_by_css_selector(
    "#root > div > div:nth-child(2) > div > div > header > div > div > div.flex.align-center.flex-align-right > span > span:nth-child(4) > a > svg").click()
driver.find_element_by_css_selector(
    "body > span.PopoverContainer.tether-element.tether-element-attached-top.tether-target-attached-bottom.tether-target-attached-center.tether-element-attached-right.tether-enabled > span > div > div > ul > li:nth-child(2) > span:nth-child(2)").click()
driver.switch_to.window(handles[1])
while True:
    # WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_by_css_selector("svg[name=\"expand\"]"))
    # WebDriverWait(driver, 20 ,0.5).until(driver.find_element_by_css_selector("svg[name=\"expand\"]"))
    driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # 到页面底部
    # js = "var q=document.documentElement.scrollTop=100000"
    # driver.execute_script(js)
    time.sleep(3)
    # driver.find_element_by_css_selector("svg[name=\"contract\"]").click()
    # driver.find_element_by_css_selector("svg.Icon.text-white").click()
    driver.switch_to.window(handles[0])
    # WebDriverWait(driver, 20, 0.5).until(driver.find_element_by_css_selector("svg[name=\"expand\"]"))
    driver.find_element_by_css_selector("svg[name=\"expand\"]").click()
    time.sleep(3)
    driver.switch_to.window(handles[1])
# driver.quit()