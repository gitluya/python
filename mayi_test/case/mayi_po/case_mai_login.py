#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Project:使用unittest框架编写测试用例。
'''
import os
import sys
import unittest
import ddt
import xlrd
from page_mai_login import PageMaiLogin
from selenium import webdriver
#通过Excel获取数据
def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

@ddt.ddt
class CaseMaiLogin(unittest.TestCase):
    """
    登录卖家后台的case
    """
    def setUp(self):
        print("===Start!===")
        # self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"  # 使用指定目录下的chromedriver
        # os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # self.driver.get("http://test.mai.mayi888.com")
        self.url = "http://test.mai.mayi888.com"
        # self.mai_mobile = "13023201619"
        # self.mai_password = "123456"

    # @ddt.data(*get_data("TestData.xlsx"))

    # 用例执行体
    @ddt.unpack
    # def test_mai_login(self):
    def test_mai_login(self, mai_phone, mai_password, error_message):
        # 声明LoginPage类对象
        mai_login_page = PageMaiLogin(self.driver, self.url, "蚂蚁手店商家助手")
        # 调用打开页面组件
        mai_login_page.open()
        # 调用用户名输入组件
        mai_login_page.input_username(self.mai_phone)
        # 调用密码输入组件
        mai_login_page.input_password(self.mai_password)
        # 调用点击登录按钮组件
        mai_login_page.click_submit()

        # errorMessage = self.driver.find_element_by_id('errorMessage').text
        # print(errorMessage)
        # self.assertEqual(error_message, error_message)  # 用assertEqual(a,b)方法来断言a == b 请输入密码等于error_message
        # curPath = os.path.abspath('.')
        # sys.path.append(curPath)
        # self.driver.get_screenshot_as_file(curPath + '/screenshot/login_pwd_null.png')

    def tearDown(self):
        self.driver.quit()
        print("===End!===")

if __name__ == "__main__":
    unittest.main()