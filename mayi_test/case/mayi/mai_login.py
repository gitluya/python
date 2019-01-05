#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import time

import ddt
# from ddt import ddt,data,unpack
import unittest
import xlrd
from selenium import webdriver

#通过Excel获取数据
def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

#运行测试脚本的时候，ddt把测试数据转换为有效的Python标识符，生成名称更有意义的测试方法。
@ddt.ddt
class MaiLogin(unittest.TestCase):#为什么类名从SearchDDT换成MaiLogin报错

    def setUp(self):

        print("Start!")
        # self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)
        # self.driver = webdriver.chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://test.mai.mayi888.com")

     #@data装饰符把参数当作测试数据，参数可以是单个值、列表、元组、字典。此@data装饰符中把元组列表作为参数。
    # @ddt.data(("13023201619", "", "请输入密码"), ("18822223333", "123456", "账号或密码输入错误！"))
    @ddt.data(*get_data("TestData.xlsx"))

    #对于列表，需要@unpack装饰符把元组和列表解析成多个参数。
    @ddt.unpack
    def test_login(self, mai_phone, mai_password, error_message):
        print(mai_phone)
        print(mai_password)
        self.driver.find_element_by_id('loginId').clear()
        self.driver.find_element_by_id('loginId').send_keys(mai_phone)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(mai_password)
        self.driver.find_element_by_id('submit').click()

        errorMessage = self.driver.find_element_by_id('errorMessage').text
        print(errorMessage)
        self.assertEqual(error_message, error_message)  # 用assertEqual(a,b)方法断言a == b
        self.driver.get_screenshot_as_file("D:/develop/python/mayi_test/screenshot/login_pwd_null.png")

    def tearDown(self):
        self.driver.quit()
        print("End!")

if __name__=='__main__':
    unittest.main(verbosity=2)
