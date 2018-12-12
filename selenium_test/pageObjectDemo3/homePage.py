#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium_test.pageObjectDemo3.base import BasePage, InvalidPageException

class HomePage(BasePage):
    _home_page_slideshow_locator = ''
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name (self._home_page_slideshow_locator)
        except:
            raise InvalidPageException ("Home Page not loaded")