#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hi_po import PageObject,PageElement
#京东首页
class JDHomePage(PageObject):
    searchInput = PageElement(id_ = 'key')
    searchButton = PageElement(xpath = '//*[@id="search"]/div/div[2]/button')