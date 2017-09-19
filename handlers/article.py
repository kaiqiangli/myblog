#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.article as articleRead
from methods.common import *
import re

class EditHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument("id", "")
        if not id.strip():
            self.render('add.html', article="")
        article = articleRead.get(id)
        article['crtTime'] = getFromatTime(article['crtTime'])
        self.render('edit.html', article=article)

class PostHandler(tornado.web.RequestHandler):
    def post(self):
        id = self.get_argument("id", "")
        content = self.get_argument("content")
        # 将多个空格替换为一个空格，不然前端htmlDecode会报错
        content = re.sub(r"\s{2,}", " ", content)
        md_content = self.get_argument("md_content")
        if not id.strip():
            articleRead.insert(md_content, content)
        else:
            articleRead.update_article(id, md_content, content)

