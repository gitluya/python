#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class HiPOUnit(unittest.TestCase):
    def __init__(self, methodName='HiPORunTest', param=None):
        super(HiPOUnit, self).__init__(methodName)
        self.param = param

        def setUp(self):
            self.verificationErrors = []
            self.accept_next_alert = True

        chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    @staticmethod
    def TestCaseWithClass(testcase_class ,lines, param=None):
        '''
        依据传入的测试类将其下面全部的测试方法加入测试套
        :param testcase_class:测试类的类名
        :param lines:参数行数（参数文件有多少行参数）
        :param param:参数池是一个dict类型
        :return:无
        '''
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        i = 0
        while i < lines:
            for name in testnames:
                suite.addTest(testcase_class(name, param=param[i]))
            i = i + 1
        return suite

    @staticmethod
    def TestCaseWithFunc(testcase_class, testcase_fun, lines, param=None):
        """
        通过给定的类及其内部的测试方法将测试用例加入测试套件中
        :param testcase_class:testcase类名
        :param testcase_fun:要执行的以test_开头的函数名
        :param lines:参数行数（参数文件有多少行参数）
        :param param:参数池是一个dict类型
        :return:无
        """
        suite = unittest.TestSuite()
        i = 0
        while i < lines:
            suite.addTest((testcase_class(testcase_fun, param=param[i])))
            i = i + 1
        return suite