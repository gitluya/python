#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import UiAutomator2 as UiAutomator2
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# automationName=UiAutomator2

driver.find_element_by_name("1").click()


driver.quit()