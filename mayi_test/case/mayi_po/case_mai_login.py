#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Project:使用unittest框架编写测试用例。
'''
import unittest
from page_mai_login import PageMaiLogin
from selenium import webdriver

class CaseMaiLogin(unittest.TestCase):
    """
    登录卖家后台的case
    """
    def setUp(self):
        # self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"  # 使用指定目录下的chromedriver
        # os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.url = "http://test.mai.mayi888.com"
        self.mai_mobile = "13023201619"
        self.mai_password = "123456"

    # 用例执行体
    def test_mai_login(self):
        # 声明LoginPage类对象
        mai_login_page = PageMaiLogin(self.driver, self.url, "蚂蚁手店商家助手")
        # login_page = PageMaiLogin(self.driver, self.url)
        # 调用打开页面组件
        mai_login_page.open()

        # 调用用户名输入组件
        mai_login_page.input_username(self.mai_mobile)
        # 调用密码输入组件
        mai_login_page.input_password(self.mai_password)
        # 调用点击登录按钮组件
        mai_login_page.click_submit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()