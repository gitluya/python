#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import xlrd
class Param(object):
    def __init__(self, paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):
        pass
    def paramColsCount(self):
        pass
    def paramHeader(self):
        pass
    def paramAllline(self):
        pass
    def paramAlllineDict(self):
        pass

class XLS(Param):
    '''
    xls基本格式（如果要把xls中存储的数字按照文本读出来，纯数字前要加上英文单引号）
    当使用XLS类解析Excel参数的时候，Excel在默认格式上有以下约束：
    1、第1行是参数的实际汉语意思。
    2、第2行是参数的变量名。
    3、第3行的参数与后面几行的参数是实际测试过程中的参数。
    4、一行是一条测试用例
    '''
    def __init__(self, paramConf):
        '''

        :param paramConf:
        '''
        self.paramConf = paramConf
        self.paramfile = self.paramConf['file'] #xls文件位置（绝对路径）
        self.data = xlrd.open_workbook(self.paramfile)
        self.getParamSheet(self.paramConf['sheet'])

    def getParamSheet(self, nsheets):
        '''
        设定参数所处的表（sheet）
        :param nsheets:
        :return:
        '''
        self.paramsheet = self.data.sheets()[nsheets]
    def getOneline(self, nRow):
        '''
        返回一行数据
        :param nRow: 行数
        :return: 一行数据[]
        '''
        return self.paramsheet.row_values(nRow)
    def getOneCol(self, nCol):
        '''
        返回一列
        :param nCol:列数
        :return: 一列数据[]
        '''
        return self.paramsheet.col_values(nCol)
    def paramRowsCount(self):
        '''
        实现Param类中的paramRowsCount
        获取参数文件行数
        :return: 参数行数 int
        '''
        return self.paramsheet.nrows
    def paramColsCount(self):
        '''
        获取参数文件列数（参数个数）
        :return: 参数文件列数（参数个数）int
        '''
        return self.paramsheet.ncols
    def paramHeader(self):
        '''
        获取参数名称
        :return: 参数名称[]
        '''
        return self.getOneline(1)
    def paramAlllineDict(self):
        '''
        获取全部参数
        :return: {{}}，其中dict的键值是header的值
        '''
        nCountRows = self.paramRowsCount()
        nCountCols = self.paramColsCount()
        ParamAllListDict = {}
        iRowStep = 2
        iColStep = 0
        ParamHeader = self.paramHeader()
        while iRowStep < nCountRows:
            ParamOneLinelist=self.getOneline(iRowStep)
            ParamOneLineDict = {}
            while iColStep < nCountCols:
                ParamOneLineDict[ParamHeader[iColStep]] = ParamOneLinelist
                [iColStep]
                iColStep = iColStep + 1
                iColStep = 0
                # print(ParamOneLineDict)
                ParamAllListDict[iRowStep - 2] = ParamOneLineDict
                iRowStep = iRowStep + 1
                return ParamAllListDict
    def paramAllline(self):
        '''
        获取全部参数
        :param self:
        :return: 全部参数[[]]
        '''
        nCountRows = self.getCountRows()
        paramall = []
        iRowStep = 2
        while iRowStep < nCountRows:
            paramall.append(self.getOneline(iRowStep))
            iRowStep = iRowStep + 1
        return paramall

    def __getParamCell(self, numberRow, numberCol):
        return self.paramsheet.cell_value(numberRow, numberCol)

class ParamFactory(object):
    '''通过MAP的键值形式，实现不同参数的调用。
    当添加一种新的参数类型的时候，仅需实现对应类型的Param子类，然后维护ParamFactory中的MAP，就可以通过简单工厂模式使用了，减少了很多代码的变动'''
    def chooseParam(self, type, paramConf):
        map_ = {
            'xls': XLS(paramConf)
        }
        return map_[type]