#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HTMLTestRunner
import time
import os
class Report(object):
    def __init__(self, testSuite, dirReport, titleReport='default', descriptionReport='default'):
        '''

        :param testSuite:
        :param dirReport:
        :param titleReport:
        :param descriptionReport:
        '''
        try:
            if not os.path.exists(dirReport):
                os.mkdir(dirReport)
                strTimeStamp = time.strftime('%Y_%m_%d %H:%M:%S')
                strTimeStamp = strTimeStamp.replace(':','_')
                titleReport = titleReport + strTimeStamp #修改成YYMMDD HH:MM:SS
                descriptionReport = descriptionReport + strTimeStamp
                filename = dirReport + titleReport + '.html'
                # filename = filename.replace(':','_')
                # print(filename)
                fp = file(filename, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(fp, title=titleReport, description=descriptionReport)
                runner.run(testSuite)
        except Exception:
            print("Please input testCase,report file's location!")