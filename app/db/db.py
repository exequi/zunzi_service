#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import lib.mylog as mylog


def execute(sql, param):
    '''执行select,update等sql'''
    with sqlite3.connect('../zundb.db') as conn:
        c = conn.cursor()
        r = []
        try:
            result = c.execute(sql, param)
            conn.commit()
            for row in result:
                r.append(row)
        except Exception as e:
            mylog.obj().warning(e)
        finally:
            c.close()
            return r


def todict(field, rows):
    '''根据制定字段返回字典数组,field数组,row 字典组成的列表'''
    rowlist = []
    for r in rows:
        tmp = {}
        for i, item in enumerate(field):
            tmp[item] = r[i]
        rowlist.append(tmp)
    return rowlist


def update(keyValue, tableName, whereParam):
    '''执行update语句,参数分别是设置值字段,表名,where字典'''
    setlist = ['%s=?' % c for c in keyValue.keys()]
    wherelist = ['%s=?' % c for c in whereParam.keys()]
    setstr = ','.join(setlist)
    wherestr = ' and '.join(wherelist)
    vallist = keyValue.values()
    vallist.extend(whereParam.values())
    sql = 'UPDATE %s SET %s WHERE %s' % (tableName, setstr, wherestr)
    return execute(sql, vallist)


def insert(keyValue, tableName, itype="INSERT INTO"):
    '''执行insert语句,参数分别是设置值字段,表名'''
    field = ','.join(keyValue.keys())
    valstr = ['?' for c in range(len(keyValue))]
    valstr = ','.join(valstr)
    vallist = keyValue.values()
    sql = '%s %s (%s)VALUES(%s)' % (itype, tableName, field, valstr)
    return execute(sql, vallist)


def select(field, tableName, whereParam):
    '''执行insert语句,参数分别是设置值字段,表名,条件字典'''
    wherelist = ['%s=?' % c for c in whereParam.keys()]
    wherestr = ' and '.join(wherelist)
    vallist = whereParam.values()
    sql = 'select %s from %s WHERE %s' % (field, tableName, wherestr)
    r = execute(sql, vallist)
    return todict(field.split(','), r)
