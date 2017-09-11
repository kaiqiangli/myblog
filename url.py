#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.user import *

url = [
    (r'/', IndexHandler),
    (r'/detail', DetailHandler),
    (r'/contact', ContactHandler),
    (r'/about', AboutHandler)
]