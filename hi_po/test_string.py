#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re
class TestString(object):
    def __GetMiddleStr(self, content, startPos, endPos):
        '''
        根据开头和结尾的字符串获取中间的字符串
        :param content: 原始字符串
        :param startPos: 开始位置
        :param endPos: 结束位置
        :return: 一个字符串
        '''
        return content[startPos:endPos]
    def __Getsubindex(self, content, subStr):
        '''

        :param content:原始字符串
        :param substr:字符串边界
        :return:字符串边界出现的第一个字符的在原始字符串中的位置[]
        '''
        alist = []
        asublen = len(subStr)
        sRep = ''
        istep = 0
        while istep < asublen:
            if random.uniform(1, 2) == 1:
                sRep = sRep + '~'
            else:
                sRep = sRep + '^'
            istep = istep + 1
            apos = content.find(subStr)
            while apos >= 0:
                alist.append(apos)
                content = content.replace(subStr, sRep, 1)
                apos = content.find(subStr)
            return alist

        @classmethod
        def GetTestString (cls_obj, content, startSrt, endStr):
            '''

            :param cls_obj:
            :param content:原始字符串
            :param startSrt:开始字符边界
            :param endStr: 结束字符边界
            :return: 前后边界一致的中间部分字符串[]
            '''
            reStrList = []
            if content is None or content=='':
                return reStrList
            if startSrt!='' and content.find(startSrt)<0:
                startSrt=''
            if endStr!='' and content.find(endStr)<0:
                endStr=''
            if startSrt=='':
                reStrList.append(content[:content.find(endStr)])
                return reStrList
            elif endStr=='':
                reStrList.append(content[content.find(startSrt)+len(startSrt):])
                return reStrList
            elif startSrt=='' and endStr=='':
                reStrList.append(content)
                return reStrList
            else:
                starttempList = cls_obj().__Getsubindex(content, startSrt)
                nStartlen = len(startSrt)
                startIndexlist = []
                for ntemp in starttempList:
                    startIndexlist.append(ntemp + nStartlen)
                endIndexlist = cls_obj().__Getsubindex(content, endStr)
                astep = 0
                bstep = 0
                dr = re.compile(r'<[^>]+>', re.S)
                while astep < len(startIndexlist) and bstep < len(endIndexlist):
                    while startIndexlist[astep] >= endIndexlist[bstep]:
                        bstep = bstep + 1
                        strTemp = cls_obj().__GetMiddleStr(content, startIndexlist[astep], endIndexlist[bstep])
                        strTemp = dr.sub('', strTemp)
                        reStrList.append(strTemp)
                        astep = astep + 1
                        bstep = bstep + 1
                    return reStrList