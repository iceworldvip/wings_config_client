# -*- coding: utf-8 -*-
# @Time     : 2018/1/17 23:50
# @Author   : ice
# @File     : test_single_process.py
# @Software : PyCharm
from __future__ import unicode_literals

import multiprocessing
import time
from unittest import TestCase


def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1


class TestSingleProcess(TestCase):

    def test_single_process(self):
        p = multiprocessing.Process(target=worker, args=(3,))
        p.start()
        print("p.pid:", p.pid)
        print("p.name:", p.name)
        print("p.is_alive:", p.is_alive())
