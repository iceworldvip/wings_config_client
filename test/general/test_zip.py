# -*- coding: utf-8 -*-
# @Time     : 2018/1/13 15:16
# @Author   : ice
# @File     : test_zip.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase


class TestZip(TestCase):

    def test_zip(self):
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        min_price = min(zip(prices.values(), prices.keys()))
        print(min_price)

        print(zip(prices.values(), prices.keys()))
        max_price = max(zip(prices.values(), prices.keys()))
        print(max_price)
