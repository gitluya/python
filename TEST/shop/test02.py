# -*- coding: utf-8 -*-
import unittest

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("开始测试")

    def test01(self):
        '''测试0201'''
        print("执行测试用例01")

    def test02(self):
        '''测试0202'''
        print("执行测试用例02")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

if __name__ == "__main__":
    unittest.main()