#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from hi_po import ParamFactory
from hi_po import Param
from hi_po import HiPOUnit
from hi_po import Report
from config.config_param import searchProcessParam
from config.config_report import reportDir, reportTitle, reportDescription
# from test_case import searchProcessParam
# from test_case import reportTitle
# from test_case import reportDescription
# from test_case import reportDir
# from test_case import TestSearchAddShoppingCart
import unittest

# 通过ParamFactory获取参数详情和参数条数，通过unittest设计测试套件，然后通过Report类获取测试报告
#设置参数
# searchParam = ParamFactory().chooseParam('xls', {'file':searchProcessParam, 'sheet':0}).paramAlllineDict()
from search_addshoppingcart import TestSearchAddShoppingCart

searchParam = Param().chooseParam('xls', {'file':searchProcessParam, 'sheet':0}).paramAlllineDict()
searchParamCount = len(searchParam)
# 设计测试
testSuite = unittest.TestSuite()
testSuite.addTests(HiPOUnit.TestCaseWithClass(TestSearchAddShoppingCart, searchParamCount, param=searchParam))
# 生成测试报告
Report(testSuite, reportDir, titleReport=reportTitle,descriptionReport=reportDescription)