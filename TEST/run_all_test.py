# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner
import time

from send_email import send_file


# 待执行用例的目录
def allcase():
    # case_dir = "E:\python\ALL_TEST\login"
    # case_dir = "D:\develop\python\TEST\login"
    case_dir = "D:\develop\python\TEST\shop"#执行的用例目录
    #case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='*.py',  #执行的文件
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    #print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase

if __name__ == "__main__":
    # runner=unittest.TextTestRunner()
    # runner.run(allcase())
    ''''''
    # 设置报告文件保存路径
    report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 设置报告名称格式
    HtmlFile = report_path + now + "HtmlReport.html"

    # report_path = r"D:\develop\reports\result.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="自动化测试unittest测试框架报告",
                                           description="用例执行情况：")

    runner.run(allcase())
    fp.close()

    send_file()  # 发送邮件!