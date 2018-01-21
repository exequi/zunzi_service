#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os


workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
print workpath
sys.path.insert(0, os.path.join(workpath, 'service\\account\\'))
print sys.path


import account1


def login1():
    account1.login()


login1()
