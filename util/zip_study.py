# -*- coding: utf-8 -*-
# @Time     : 2018/1/13 15:16
# @Author   : ice
# @File     : zip_study.py
# @Software : PyCharm


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

if __name__ == '__main__':
    min_price = min(zip(prices.values(), prices.keys()))
    print min_price

    print zip(prices.values(), prices.keys())
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)
