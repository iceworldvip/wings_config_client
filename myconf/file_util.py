# -*- coding: utf-8 -*-
# @Time     : 2018/1/12 9:03
# @Author   : ice
# @File     : config_util.py
# @Software : PyCharm
import os
import mmap

from project_path import PROJECT_PATH

if __name__ == '__main__':
    file_path = (PROJECT_PATH + os.path.sep + "conf" + os.path.sep)
    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)
    #
    with open(file_path + "test.txt", "rb+") as f:

        mm = mmap.mmap(f.fileno(), 0)

