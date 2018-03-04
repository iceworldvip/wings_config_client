# -*- coding: utf-8 -*-
# @Time     : 2018/1/20 23:48
# @Author   : ice
# @File     : tree_study.py
# @Software : PyCharm

a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
    ]


class BinaryTree(object):
    def __init__(
            self,
            left,
            right
            ):
        self.left = left
        self.right = right


class MultiTree(object):
    def __init__(
            self,
            kids,
            next=None
            ):
        self.kids = self.val = kids
        self.next = next


class Bunch(dict):
    def __init__(
            self,
            *args,
            **kwargs
            ):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self
