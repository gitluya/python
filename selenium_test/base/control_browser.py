# -*- encoding:utf-8 -*-
 ## 引入WebDriver的包
from time import sleep
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
# 去掉 "chrome正受到自动测试软件的控制" 警告框
chromeOptions = webdriver.ChromeOptions()
# chromeOptions._arguments = ['disable-infobars']
chromeOptions.add_argument('disable-infobars') # 去掉 "chrome正受到自动测试软件的控制" 警告框
chromeOptions.add_argument('--kiosk') # 全屏
# chromeOptions.add_argument('start-fullscreen') # 全屏2
# chromeOptions.add_argument('allow-running-insecure-content') # 全屏2
# chromeOptions.add_argument('--test-type') # 全屏2
driver = webdriver.Chrome(chrome_options=chromeOptions)

# driver = webdriver.Chrome()#谷歌(只用这一句的话，用的好像是python安装目录下的chromedriver)
# 使用指定目录下的chromedriver（？环境变量PATH中没配置也可以）
# chromedriver = "C:/Users/yaya/AppData/Local/Google/Chrome/Application/chromedriver.exe"
chromedriver = "C:/chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver

 ## 创建浏览器对象
# driver = webdriver.Chrome(chromedriver)
# driver.maximize_window()
## 导航到百度主页
driver.get('https://www.baidu.com')
## 检查标题是否为‘百度一下，你就知道’
assert '百度一下，你就知道' in driver.title
## 找到名字为wd的元素，赋值给elem
kw = "#kw"
# elem = driver.find_element_by_name('wd')  # 找到搜索框
# elem.send_keys('selenium' + Keys.RETURN)  # 搜索selenium
# driver.find_element_by_id("kw").send_keys(Keys.F11)
# sleep(3)
# driver.execute_script("window.open('http://news.baidu.com/')","")
# handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
# driver.switch_to.window(handles[0])
# driver.find_element_by_id("kw").send_keys(Keys.SHIFT,"Selenium")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#到页面底部
driver.find_element_by_css_selector(kw).send_keys(Keys.SHIFT,"Selenium")

driver.find_element_by_id("kw").send_keys(Keys.F11)
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
sleep(3)
## 关闭浏览器
driver.quit()