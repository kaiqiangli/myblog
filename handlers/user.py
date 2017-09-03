#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrb
import methods.article as articleRead

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        user_infos = mrb.select_table(table="users",column="*",condition="username",value=username)
        # self.render("user.html", users = user_infos)
        userId = user_infos[0]['id']
        articles = articleRead.query_article(userId, 0, 10)
        self.render('article.html', articles = articles)