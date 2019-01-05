#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver

user_name = "ms.zhao"
password = "888888"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.mayi.mayi_saler_app'
desired_caps['appActivity'] = '.view.activity.StartActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动APP
print("start")
sleep(3)
driver.find_element_by_id("com.mayi.mayi_saler_app:id/login_activity_user_name_et").send_keys(user_name)
driver.find_element_by_id("com.mayi.mayi_saler_app:id/login_activity_user_pass_word_et").send_keys(password)
driver.hide_keyboard()#隐藏键盘
sleep(0.5)
driver.find_element_by_id("com.mayi.mayi_saler_app:id/login_activity_login_ack_btn").click()


driver.quit()
print("end")