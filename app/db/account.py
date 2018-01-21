#!/usr/bin/python
# -*- coding: UTF-8 -*-

import db


def findPublic(id):
    field = "id,account,photo,nick,ismale,age,sign"
    r = db.execute('SELECT %s from user_account where id=?' % (field), (id,))
    r = db.todict(field.split(','), r)
    return r


def checkpwd(account, password):
    field = "id,account,photo,nick,ismale,age,sign"
    r = db.select(field, 'user_account', {
                  'account': account, 'password': password})
    return r


def update(accountinfo, id):
    r = db.update(accountinfo, 'user_account', {'id': id})
    return r


def register(accountinfo):
    r = db.insert(accountinfo, 'user_account')
    return r

#print checkpwd('111', 'b')
#print db.execute("UPDATE user_account set nick='omg' where id=? and account=?", (1,111,))


#update({'nick': 'obj', 'account': '111'}, 1)
#register({'account': 'obj2','password':'111','nick':'1', 'id': '223'})
