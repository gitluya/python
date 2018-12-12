#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于存放测试报告的一些通用配置，在项目路径中，要按照报告配置文件的路径配置建立报告存储目录
import sys
import os
# 获取当前项目路径
curPath = os.path.abspath('.')
sys.path.append(curPath)
# 所有全局参数都写在这个文件内
'''报告相关参数：报告文件的文件夹绝对地址（最后一层文件夹可以不存在）：命名系统功能（或功能名称）_reportDir'''
'''     报告名称：命名 系统功能（或功能名称）_titleReport'''
'''     报告描述：命名 系统功能（或功能名称）_descriptionReport'''
reportDir = curPath + '/test_report/'
reportTitle = u'PO框架自动化测试报告：浏览商品加入购物车'
reportDescription = u'PO框架自动化测试报告：浏览商品加入购物车'