#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.article as articleRead
from methods.common import *

# 文章详情页
class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        articles = articleRead.query_article(0, 10)
        categorys = articleRead.query_category()
        recentArticles = articleRead.query_recent_article()
        id = self.get_argument("id")
        article = articleRead.get(id)
        article['crtTime'] = getFromatTime(article['crtTime'])

        self.render('single.html',article = article, articles = articles, categorys = categorys, recentArticles = recentArticles)

# 联系我们
class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('contact.html')

# 关于
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')
