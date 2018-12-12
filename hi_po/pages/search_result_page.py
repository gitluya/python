#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hi_po import PageObject,MultiPageElement
#搜索结果页
class JDsearchResultPage(PageObject):
    resultList = MultiPageElement(xpath='//*[@id="J_goodsList"]/ul/li/div/div[3]/strong/i')