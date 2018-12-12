from selenium import webdriver

import os

IEDriverServer = "C:/Program Files/Internet Explorer/IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = IEDriverServer

browser = webdriver.Ie(IEDriverServer)
## 导航到百度主页
browser.get('https://www.baidu.com')

## 检查标题是否为‘百度一下，你就知道’
assert '百度一下，你就知道' in browser.title

## 找到名字为wd的元素，赋值给elem
elem = browser.find_element_by_name('wd')  # 找到搜索框
elem.send_keys('selenium' + Keys.RETURN)  # 搜索selenium

## 关闭浏览器
# browser.quit()