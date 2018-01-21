#!/usr/bin/python
# -*- coding: UTF-8 -*-


import md5
import uuid
import datetime


def secret(txt):
    salt = 'Vk89FA44BrIvoNeM1DIi715P0ppyWXxF'
    '''md5加密字符串'''
    return md5.md5(txt + salt).hexdigest()


def uid():
    '''生成32位唯一id'''
    return uuid.uuid1().hex


def now():
    t = datetime.datetime.now()
    return t.strftime('%Y-%m-%d %H:%M:%S')


def checkparam(requestform, filterfield, mustfield=[]):
    r = {}
    code = 0
    missfiled = []
    for ft in filterfield:
        if ft in requestform:
            r[ft] = requestform[ft]
    for mt in mustfield:
        if mt not in requestform:
            missfiled.append(mt)
            code = -1
    return (code, r, missfiled)
