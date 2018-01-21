#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mylog


class error(Exception):
    '''自定义异常,使用示例
        from error import *
        raise error('error msg',100)'''
    def __init__(self, msg, code=-1):
        Exception.__init__(self)
        self.msg = 'code:%s,msg:%s' % (code, msg)
        mylog.obj().warning(msg)

    def __str__(self):
        return "customer exception,%s" % self.msg
