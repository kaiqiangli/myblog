#!/usr/bin/env python
# coding=utf-8
import time


def getFromatTime(a):
    return time.strftime("%d %B %Y", a.timetuple())

