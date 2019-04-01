# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner
import time
from imp import reload
from send_email import send_file
from bs4 import BeautifulSoup
import sys

# 待执行用例的目录
def allcase():
    case_dir = "D:\develop\python\TEST\shop" #需要变为相对路径
    #case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='*login.py',  #执行的文件
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    #print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase

# def HtmlFile(args):
#     # 设置报告文件保存路径
#     report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
#     # 获取系统当前时间
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     # 设置报告名称格式
#     HtmlFile, type= report_path + now + "HtmlReport.html"  #type解决TypeError: expected str, bytes or os.PathLike object, not function
#     print(HtmlFile)
#     return HtmlFile
#     # pass

if __name__ == "__main__":
    # runner=unittest.TextTestRunner()
    # runner.run(allcase())
    # report_path = r"D:\develop\reports\result.html"
    report_path = r"D:\develop\python\test_report\HtmlReport.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="自动化测试unittest测试框架报告",
                                           description="用例执行情况：")
    runner.run(allcase())
    fp.close()
    # send_file()  # 发送邮件!

#========
reload(sys)
# sys.setdefaultencoding('utf8')#Python3字符串默认编码unicode, 所以sys.setdefaultencoding也不存在了
def is_result_pass():
    try:
        with open(r"D:\develop\python\test_report\HtmlReport.html", "rb") as fp:
            f = fp.read()  # 读报告
        soup = BeautifulSoup(f, "html.parser")
        status = soup.find_all(class_="attribute")
        result = status[2].contents[-1] # 获取报告结果
        if "Failure" in result or "Error" in result:
            print("测试过程有不通过用例：%s"%result)
            return False
        else:
            return True
    except Exception as msg:
        print("判断过程出现异常：%s"%str(msg))
        return False

if __name__ == "__main__":
    res = is_result_pass()
    print(res)

if not is_result_pass():
    # 判断html报告是否有报错

    # 执行发送邮件函数，自己写一个发邮件函数
    # send_mail(sender, psw, receiver, smtp_server, report_file)
    send_file()  # 发送邮件!

else:
    print("测试用例全部通过，不发送邮件")

#========
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr(( \
#         Header(name, 'utf-8').encode(), \
#         addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#
# ## ==============定义发送附件邮件==========
# def send_file(HtmlFile):
#     smtpserver = 'smtp.qq.com'
#     user = '875914261@qq.com' #发件人邮箱账号
#     password = 'nbtthquawshabahj' #qq授权码  设置>>账户>>开启服务 获取授权码
#     sender = '875914261@qq.com'
#     receiver = ['lu.ya@mayi888.com','875914261@qq.com'] #收件人邮箱账号
#
#     # # 设置报告文件保存路径
#     # report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
#     # # 获取系统当前时间
#     # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     # # 设置报告名称格式
#     # HtmlFile = report_path + now + "HtmlReport.html"
#     # import run_all_test
#     HtmlFile = HtmlFile()
#     file = open(HtmlFile, 'rb').read()
#     subject = '自动化测试报告--微商城访问'
#
#     att = MIMEText(file, "html", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["ContenT-Disposition"] = "attachment;filename = HtmlReport.html"
#
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject
#     msgRoot['From'] = _format_addr(u'自动化测试<%s>' % sender)
#     msgRoot['To'] = _format_addr(u'收件人<%s>' % receiver)
#     # msgRoot.attach(att)
#     msgRoot.attach(att)
#
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user, password)
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()
#
# send_file(HtmlFile)  # 发送邮件!
#========