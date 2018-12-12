#!/usr/bin/env python
# -*- coding: utf-8 -*-
from builtins import object
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

#查找页面元素的方法枚举
_LOCATOR_MAP = {'css' : By.CSS_SELECTOR ,
                'id_' : By.ID ,
                'name' : By.NAME ,
                'xpath' : By.XPATH ,
                'link_text' : By.LINK_TEXT ,
                'partial_link_text' : By.PARTIAL_LINK_TEXT ,
                'tag_name' : By.TAG_NAME ,
                'class_name' : By.CLASS_NAME ,
                }
class PageObject(object):
    """
    在PageObject类中调用Webdriver
    :param webdriver: 'selenium.webdriver.WebDriver',Selenium webdriver的实例
    :param root_uri: 所有访问的基础URI，在调用PageObject.get方法后，都会拼接root_uri。
                    在调用中如果没有显示给root_uri赋值，那么将会在传入的WebDriver实例中进行查找
    """
    def __init__(self, webdriver, root_uri = None):
        self.driver = webdriver
        self.root_uri = root_uri if root_uri else getattr(self.w, 'root_uri', None)

    def get(self, uri):
        '''
        :param uri: 所有get请求的父URI
        :return:
        '''
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)

    #PageObject中加入的3个成员变量
    def getTitle(self):
        '''
        获取当前页面的title，方便在测试过程进行页面跳转的检测
        :return: return the page title
        '''
        return self.driver.title

    def switchTo(self, loc):
        '''
        整合了在iframe或者window之间的跳转
        :param loc: frame or windows name,id and so on
        :return:
        '''
        try:
            self.driver.switch_to.frame(loc)
        except:
            try:
                self.driver.switch_to.window(loc)
            except:
                print('Error: no can switch to element')

    def acceptAlert(self):
        '''
        用于接受一些警告
        :return:
        '''
        self.driver.switch_to.alert().accept()

class PageElement(object):
    """
    PageElement和MultiPageElement类用于处理页面的元素。
    PageElement类返回一个元素，MultiPageElement类返回一组具有相同locator的元素。
    PageElement通过locator定位后，返回一个WebElement类型的实例。通过该实例就可以直接调用全部WebDriver的WebElements的api对页面的元素进行操作了。
    """
    def __init__(self, context=False, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def find(self, context):
        try:
            return context.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None
        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)
        if not context:
            context = instance.driver
        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support element with context.")
        elem = self.__get__(instance, instance._class_)
        if not elem:
            raise ValueError("Can't set value,element not found.")
        elem.send_keys(value)

class MultiPageElement(PageElement):
    """

    """
    def find(self, context):
        try:
            return context.find_element(*self.locator)
        except NoSuchElementException:
            return []

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry,the set descriptor dosen't support elements with context.")
        elems = self.__get__(instance, instance._class_)
        if not elems:
            raise ValueError("Can't set value,element not found.")
        [elem.send_keys(value) for elem in elems]
class GroupPageElement (MultiPageElement):
    """
    用于获取一组相关的页面元素。（当前仅支持XPath的查找）
    用法举例：例如，在页面上有一个下拉框,
    <select id="success" name="success" class="form-control search-select" width="180px">
        <option>成功</option>
        <option>失败</option>
    </select>
    执行语句selectSuccess = GroupPageElement(xpath='//*[@id="success"]/option')查找这一组页面元素，就可以定位任意一个下拉框中的内容。
    如果选择“成功”，那么selectSuccess.[u'成功'].click()就完成了单击。
    """
    def find(self, context):
        try:
            dicGroup = {}
            for aElement in context.find_element(*self.locator):
                dicGroup[aElement.text] = aElement
            return dicGroup
        except NoSuchElementException:
            return {}

    def __set__(self, instance, value):
        if self.has_context :
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance._class_)
        if not elems :
            raise ValueError("Can't set value, no elements found.")
        [elem.send_keys(value) for elem in elems]

page_element = PageElement
multi_page_element = MultiPageElement