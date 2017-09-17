#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.article as articleRead
from methods.common import *


class EditHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument("id")
        article = articleRead.get(id)
        article['crtTime'] = getFromatTime(article['crtTime'])
        self.render('edit.html', article=article)

class PostHandler(tornado.web.RequestHandler):
    def post(self):
        id = self.get_argument("id")
        content=self.get_argument("content")
        md_content = self.get_argument("md_content")
        articleRead.update_article(id,md_content,content)
        # self.render('index.html')
