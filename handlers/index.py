#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import methods.article as articleRead
from methods.common import *
import datetime

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[0]['username']
        articles = articleRead.query_article(0, 6)

        for article in articles:
            article['crtTime'] = getFromatTime(article['crtTime'])

        categroys = articleRead.query_category()
        recentarticles = articleRead.query_recent_article()
        features = articleRead.query_features()
        self.render("index.html", articles = articles , user=one_user, categorys = categroys, recentArticles = recentarticles, features = features)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0]['password']
            if db_pwd == password:
                self.write(username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")