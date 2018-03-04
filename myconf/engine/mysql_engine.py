# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 20:12
# @Author   : ice
# @File     : mysql_engine.py
# @Software : PyCharm
from __future__ import unicode_literals

import logging

from myconf.engine.engine import AbstractEngine


class MySQLEngine(AbstractEngine):
    """
    MySQL数据库连接引擎
    """

    def __init__(self,
            uri,
            sqlalchemy_connector=None,
            **kwargs):
        if not sqlalchemy_connector:
            pass

    def connect(self):
        logging.info("Mysql连接成功")
        pass
