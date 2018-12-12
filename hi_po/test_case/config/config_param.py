#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于存储测试过程中的参数文件路径
import sys
import os
# 获取当前项目路径
curPath = os.path.abspath('.')
sys.path.append(curPath)
# 所有全局参数都写在这个文件内
searchProcessParam = curPath + '/test_case/param/searchkeyword.xls'