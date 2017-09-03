#!/usr/bin/env python
# coding=utf-8

import pymysql

#连接对象
DB_CONN = pymysql.connect(host='localhost',port=3306,user = 'root',passwd='139631',db='user',charset="utf8")

cursor = DB_CONN.cursor(pymysql.cursors.DictCursor)