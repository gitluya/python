#!/usr/bin/env python
# -*- coding: utf-8 -*-
#期望达到的效果：
from telnetlib import EC

from selenium import webdriver
from time import sleep
import os
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chromedriver = r"C:/Users/root/AppData/Local/Google/Chrome/Application/chromedriver.exe" #待优化
os.environ["webdriver.chrome.driver"] = chromedriver

class ShopIndex(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)  # 隐性等待，最长等30秒
        # self.driver.maximize_window()
        self.driver.set_window_size(375,750)
        # self.driver.refresh()

    # 定义登录商城方法
    def shopIndex(self,shopUrl,title,usernameInput,username,password):
        self.driver.get(shopUrl)
        print(shopUrl)
        self.assertEqual(title, self.driver.title)
        self.driver.find_element_by_link_text("我的").click()
        # WebDriverWait(self.driver, 20, 0.5).until(
        #     EC.presence_of_element_located((By.XPATH, usernameInput)))#加这一句会跳过下面的步骤？？？
        self.driver.find_element_by_xpath(usernameInput).clear()
        self.driver.find_element_by_xpath(usernameInput).send_keys(username)
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_css_selector("button.mm_btn").click()
        self.assertEqual(title, self.driver.title)#断言标题

    def test_shop1(self):
        '''明丞子商城'''
        self.shopIndex("https://m.mingchengzi.com/yixidao",u"明丞子",
                       "// *[ @ id = 'yixidao'] / section / div[2] / div[1] / div / div / div / input",
                       "13023201619","123456")
        self.driver.get_screenshot_as_file('D:/develop/python/screenshots/title.png')
        sleep(2)
        print('明丞子商城')

    def test_shop2(self):
        '''Tjus商城'''
        self.shopIndex("http://tjus.justfortee.com/tjus/",u"Tjus",
                       "// *[ @ id = 'tjus'] / section / div[1] / div[1] / div / div / div / input",
                       "13023201619","123456")
        sleep(2)
        print('Tjus商城')

    @classmethod
    def tearDownClass(self):
        print('test pass！')
        self.driver.quit()

        # setUpClass():必须使用@classmethod 装饰器,所有test运行前运行一次
        # tearDownClass():必须使用@classmethod装饰器,所有test运行完后运行一次
        # setup():每个测试函数运行前运行
        # teardown():每个测试函数运行完后执行

if __name__ == "__main__":
    unittest.main()