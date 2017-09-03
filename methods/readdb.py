#!/usr/bin/env python
# coding=utf-8

from db_con import *

def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines

def select_columns(table, column ):
    sql = "select " + column + " from " + table
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines