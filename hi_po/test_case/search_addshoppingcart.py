#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1、进入京东首页，在搜索栏中输入“决战618”，单击搜索按钮。
2、在搜索结果页单击第一个搜索结果。
3、进入商品详情页，检查商品名称，获取页面title后，选择“白条分期”后面的“不分期”选项，并单击“加入购物车”按钮。
'''
import time
from selenium import webdriver
from config.config_uri import test_uri
from pages import home_page, search_result_page, ware_detail


class TestSearchAddShoppingCart(object):
    def setUp(self):
        print("Start!")
        # self.driver = webdriver.Firefox()
        # chromedriver = "C:/chromedriver.exe"
        # self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Chrome(executable_path="c:\\chromedriver")
        # self.driver = webdriver.chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(test_uri)

    def testSearchAddShoppingCart(self):
        home = home_page(webdriver)
        home_page.JDHomePage.searchInput.sendkey("决战618")
        # search_result_page.JDsearchResultPage.
        driver = self.driver
        driver.find_element_by_id("J-toolbar-load-hook").click()
        driver.find_element_by_id("J-toolbar-load-hook").click()
        driver.find_element_by_id("key").clear()
        driver.find_element_by_id("key").send_keys(u"决战618")
        driver.find_element_by_css_selector("button.button").click()
        driver.find_element_by_id("J-toolbar-load-hook").click()
        driver.find_element_by_css_selector("font.skcolor_ljg").click()
        driver.find_element_by_xpath(
            "//li[@onclick='log(\"gz_item\", \"gz_detail\",\"02\",\"zjzh_dh\",\"null\",\"main\")']").click()
        driver.find_element_by_css_selector("span.name").click()
        driver.find_element_by_id("InitCartUrl").click()
        driver.find_element_by_xpath(
            "(//a[contains(@href, '//cart.jd.com/gate.action?pid=12202253&pcount=1&ptype=1&ybId=31810060776')])[3]").click()

    def tearDown(self):
        self.driver.quit()
        print("End!")