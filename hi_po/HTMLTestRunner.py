#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
如果中文乱码，需要修改\Python\Python37-32\Lib\HTMLTestRunner.py中的源码。大概764行

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o,str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            # uo = o.decode('latin-1')
            # uo = e 原来的
            uo = o.decode('utf-8')
        else:
            uo = o
        if isinstance(e,str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            # ue = e.decode('latin-1')
            # ue = e 原来的
            ue = e.decode('utf-8')
        else:
            ue = e
'''