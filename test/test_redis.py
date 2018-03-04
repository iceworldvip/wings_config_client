# -*- coding: utf-8 -*-
# @Time     : 2018/3/5 9:27
# @Author   : ice
# @File     : test_redis.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

import redis


class TestRedis(TestCase):
    def test_redis_connect(self):
        redis_pool = redis.ConnectionPool(host='192.168.31.18', port=6379)
        redis_client = redis.StrictRedis(connection_pool=redis_pool)
        redis_client.get('name')
