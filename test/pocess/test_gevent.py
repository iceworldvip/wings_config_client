# -*- coding: utf-8 -*-
# @Time     : 2018/3/5 23:05
# @Author   : ice
# @File     : test_gevent.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

import gevent
from gevent import monkey

monkey.patch_socket()


class TestGevent(TestCase):
    def test_gevent(self):
        def func(n):
            for i in xrange(10):
                print(gevent.getcurrent(), i)
                gevent.sleep(0)

        g1 = gevent.spawn(func, 5)
        g2 = gevent.spawn(func, 5)
        g3 = gevent.spawn(func, 5)
        g1.join()
        g2.join()
        g3.join()
