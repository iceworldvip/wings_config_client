# -*- coding: utf-8 -*-
# @Time     : 2018/1/13 15:32
# @Author   : ice
# @File     : dict_study.py
# @Software : PyCharm


a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
if __name__ == '__main__':
    print set(a.keys()) & set(b.keys())
