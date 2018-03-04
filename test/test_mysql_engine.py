# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 20:13
# @Author   : ice
# @File     : test_mysql_engine.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

from myconf.engine.mysql_engine import MySQLEngine


class TestMySQLEngine(TestCase):
    def test_connect(self):
        MySQLEngine
