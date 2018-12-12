#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ddt
import unittest
# from ddt import ddt,data,unpack
from selenium import webdriver

#运行测试脚本的时候，ddt把测试数据转换为有效的Python标识符，生成名称更有意义的测试方法。
@ddt.ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        print("Start!")
        # self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)
        # self.driver = webdriver.chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com")

     #@data装饰符把参数当作测试数据，参数可以是单个值、列表、元组、字典。此@data装饰符中把元组列表作为参数。
    @ddt.data(("phones", 2), ("music", 5))

    #对于列表，需要@unpack装饰符把元组和列表解析成多个参数。在test_search()方法中，search_value与expected_count两个参数用来接收元组解析的数据。
    @ddt.unpack
    def test_search(self, search_value, expected_count):
        print(search_value)
        print(expected_count)
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(expected_count, len(products))
    def tearDown(self):
        self.driver.quit()
        print("End!")

if __name__=='__main__':
    unittest.main(verbosity=2)
