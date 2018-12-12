#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod

class BasePage(object):
    """All page objects inherit from this"""
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    """Regions define functionality available through all page objects"""
    @property
    def search(self):
        from search import searchRegion
        return SearchRegion(self.driver)

class InvalidPageException(Exception):
    """Throw this exception when you don't find the correct page"""
    pass