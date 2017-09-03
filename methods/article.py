#!/usr/bin/env python
# coding=utf-8

from db_con import *

# 查询用户文章列表
def query_article(userid, startPos, pageSize):
    print "userid = %d" %( userid )
    sql = "select * from Article where userId = %d and deleted = 0 limit %d,%d" %(userid, startPos, pageSize)
    cursor.execute(sql)
    articles = cursor.fetchall()
    return articles