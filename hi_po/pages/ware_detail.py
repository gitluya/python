#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hi_po import PageObject,PageElement,MultiPageElement,GroupPageElement
#商品详情页
class WareDetailPage(PageObject):
    # 加入购物车变量
    addShoppingCart = PageElement(id_ = 'choose-btn-append')
    wareName = PageElement(id_ = 'name')
    # 白条分期变量
    # 应用了GroupPageElement，引用XPath的locator定位这一组元素。
    # 当应用GroupPageElement定位元素的时候，传入XPath能够找到的一定是文本，因为其中的文本是定位一个元素的key值。
    repaymentType = GroupPageElement(xpath='//*[@id="choose-baitiao"]/div[2]/[div[1]/div/a/strong')