#!/usr/bin/python
# -*- coding: UTF-8 -*-

import lib.tool as tool
import lib.mylog as mylog
import db.account


def register(param):
    mylog.obj().info('222')
    fd = ['account', 'password']
    p = tool.checkparam(param, fd, fd)
    if p[0] == 0:
        p[1]['id'] = tool.uid()
        if 'nick' not in p[1]:
            p[1]['nick'] = 'nick'
        db.account.register(p[1])
    # print p
    return str(p[0])