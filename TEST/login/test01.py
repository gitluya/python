# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
import unittest

chromedriver = r"C:/Users/root/AppData/Local/Google/Chrome/Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.refresh()
        
 
    # 定义登录方法
    def login(self, loginId, password):
        self.dr.get('http://test.mai.mayi888.com/')  # 登录页面
        self.dr.find_element_by_id('loginId').send_keys(loginId)
        self.dr.find_element_by_id('password').send_keys(password)
        self.dr.find_element_by_id('submit').click()

 
    def test_login_1_user_null(self):
        '''用户名为空、密码正确'''
        self.login(' ', '888888')
        error_message = self.dr.find_element_by_id('errorMessage').text
        self.assertEqual(error_message,'账号不能为空！')  # 用assertEqual(a,b)方法来断言  a == b
        sleep(2)
        print('用户空，登录失败')
    
    def test_login_2_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('13012345666', ' ')
        error_message = self.dr.find_element_by_id('errorMessage').text
        self.assertEqual(error_message,'密码不能为空！')  # 用assertEqual(a,b)方法来断言a == b 请输入密码等于error_message
        sleep(2)
        print('密码空，登录失败')


    # def test_login_3_pwd_error(self):
    #     '''用户名正确、密码不正确'''
    #     self.login('13012345666', '123456')
    #     error_message = self.dr.find_element_by_id('errorMessage').text
    #     self.assertIn('账号或密码输入错误！', error_message)  # 用assertIn(a,b)方法来断言 a in b  '账号或密码输入错误！'在error_message里
    #     sleep(2)
    #     print('密码错误，登录失败')
 
    # def test_login_4_user_error(self):
    #     '''用户名错误、密码正确'''
    #     self.login('1301234678', '888888')
    #     error_message = self.dr.find_element_by_id('errorMessage').text
    #     self.assertIn('请输入正确的登录账号(手机号)！', error_message)  # 用assertIn(a,b)方法来断言 a in b
    #     sleep(2)
    #     print('用户名错误，登录失败')
    
    # def test_login_5_success(self):
    #     '''用户名、密码正确'''
    #     self.login('13012345666', '888888')
    #     #assert '蚂蚁手店商家助手' in browser.title
    #     sleep(2)
    #     print('登录成功')


    @classmethod
    def tearDownClass(self):   
        print('test pass！')
        self.dr.quit()

        #setUpClass():必须使用@classmethod 装饰器,所有test运行前运行一次
        #tearDownClass():必须使用@classmethod装饰器,所有test运行完后运行一次
        #setup():每个测试函数运行前运行
        #teardown():每个测试函数运行完后执行
        
if __name__ == "__main__":
    unittest.main()