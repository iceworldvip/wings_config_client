# -*- coding: utf-8 -*-
# @Time     : 2018/1/18 9:05
# @Author   : ice
# @File     : test_multi_process.py
# @Software : PyCharm
from __future__ import unicode_literals

import multiprocessing
import time
from unittest import TestCase


def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("end worker_1")


def worker_2(interval):
    print("worker_2")
    time.sleep(interval)
    print("end worker_2")


def worker_3(interval):
    print("worker_3")
    time.sleep(interval)
    print("end worker_3")


class TestMultiProcess(TestCase):

    def test_multi_process(self):
        p1 = multiprocessing.Process(target=worker_1, args=(2,))
        p2 = multiprocessing.Process(target=worker_2, args=(3,))
        p3 = multiprocessing.Process(target=worker_3, args=(4,))

        p1.start()
        p2.start()
        p3.start()

        print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        for p in multiprocessing.active_children():
            print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
        print("END!!!!!!!!!!!!!!!!!")
