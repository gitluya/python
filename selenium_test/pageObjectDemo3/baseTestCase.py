#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import time

import unittest
import ddt
from selenium import webdriver

@ddt.ddt
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print("Start!")
        # self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)
        # self.driver = webdriver.chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # self.driver.get("http://test.mai.mayi888.com")
        self.driver.get("http://demo.magentocommerce.com")

    def tearDown(self):
        self.driver.quit()
        print("End!")