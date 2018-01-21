#!/usr/bin/python
# -*- coding: UTF-8 -*-
import db.tool
import db.account

def login():
    return "login in"


def register(param):
    fd = ['account', 'password']
    p = db.tool.checkparam(param, fd, fd)
    if p[0] == 0:
        p[1]['id'] = db.tool.uid()
        if 'nick' not in p[1]:
            p[1]['nick'] = 'nick'
        db.account.register(p[1])
    # print p
    return str(p[0])