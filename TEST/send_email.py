# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from numpy.core import unicode
import os
import time

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

## ==============定义发送附件邮件==========
def send_file():
    smtpserver = 'smtp.qq.com'
    user = '875914261@qq.com' #发件人邮箱账号
    password = 'nbtthquawshabahj' #qq授权码  设置>>账户>>开启服务 获取授权码
    sender = '875914261@qq.com'
    receiver = 'lu.ya@mayi888.com' #收件人邮箱账号

    # # 设置报告文件保存路径
    # report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
    # # 获取系统当前时间
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # # 设置报告名称格式
    # HtmlFile = report_path + now + "HtmlReport.html"
    import run_all_test
    file = open(run_all_test.HtmlFile, 'rb').read()
    subject = '自动化测试报告--微商城访问'

    att = MIMEText(file, "html", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["ContenT-Disposition"] = "attachment;filename = result.html"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = _format_addr(u'自动化测试<%s>' % sender)
    msgRoot['To'] = _format_addr(u'收件人<%s>' % receiver)
    # msgRoot.attach(att)
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()