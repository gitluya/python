#!/usr/bin/env python
# -*- coding: utf-8 -*-
#期望达到的效果：通过外部文件读取商城首页地址，访问该首页，判断首页访问是否正常，截图。执行结束后，生成报告并发送邮件
from selenium import webdriver
from time import sleep
import os
import unittest

chromedriver = r"C:/Users/root/AppData/Local/Google/Chrome/Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

class ShopIndex(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        # self.dr.maximize_window()
        self.dr.set_window_size(375,750)
        # self.dr.refresh()

    # 定义访问商城首页方法
    def shopIndex(self,shopUrl):

        self.dr.get(shopUrl)
        print(shopUrl)

    def test_shop1(self):
        '''明丞子商城首页'''
        self.shopIndex("https://m.mingchengzi.com/yixidao")
        # error_message = self.dr.find_element_by_id('errorMessage').text
        # self.assertEqual(error_message, '账号不能为空！')  # 用assertEqual(a,b)方法来断言  a == b
        title = self.dr.title
        print(title)
        self.dr.get_screenshot_as_file('/Screenshots/title.png')
        sleep(2)
        print('明丞子商城')

    def test_shop2(self):
        '''Tjus商城首页'''
        self.shopIndex("http://tjus.justfortee.com/tjus/")
        # error_message = self.dr.find_element_by_id('errorMessage').text
        # self.assertEqual(error_message, '账号不能为空！')  # 用assertEqual(a,b)方法来断言  a == b
        sleep(2)
        print('Tjus商城')

    @classmethod
    def tearDownClass(self):
        print('test pass！')
        self.dr.quit()

        # setUpClass():必须使用@classmethod 装饰器,所有test运行前运行一次
        # tearDownClass():必须使用@classmethod装饰器,所有test运行完后运行一次
        # setup():每个测试函数运行前运行
        # teardown():每个测试函数运行完后执行


if __name__ == "__main__":
    unittest.main()