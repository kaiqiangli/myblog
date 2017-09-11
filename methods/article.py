#!/usr/bin/env python
# coding=utf-8

from db_con import *

# 查询用户文章列表
def query_article(startPos, pageSize):
    sql = "select * from Article where deleted = 0 limit %d,%d" %(startPos, pageSize)
    cursor.execute(sql)
    articles = cursor.fetchall()
    return articles

# 查询热门文章
def query_features():
    sql = "select id,title,summary from Article where deleted = 0 order by commendsCount desc limit 5"
    cursor.execute(sql)
    features = cursor.fetchall()
    return features

# 根据文章编号查询文章
def get(id):
    sql = "select * from Article where deleted = 0 and id = %s" %id
    cursor.execute(sql)
    article= cursor.fetchall()[0]
    return article

# 查询分类
def query_category():
    sql = "select category.id, category.name, category.comment from user.Category category where category.deleted = 0"
    cursor.execute(sql)
    categorys = cursor.fetchall()
    return categorys

# 查询最近文章列表
def query_recent_article():
    sql = "select * from Article where deleted = 0 and crtTime > date_sub(current_date(), INTERVAL 15 day) order by 1 desc limit 5"
    cursor.execute(sql)
    recent = cursor.fetchall()
    return recent

