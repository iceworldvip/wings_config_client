# -*- coding: utf-8 -*-
# @Time     : 2018/5/18 9:54
# @Author   : ice
# @File     : file_util.py
# @Software : PyCharm
from __future__ import unicode_literals

import logging
import os
import platform

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG
)


class FileUtil(object):

    @classmethod
    def get_file(cls, path):
        if not path:
            return False
        logging.info(os.path.split(path))
        with open(path) as f:
            logging.info(f.read())
            logging.info(os.path.split(f.name.encode())[1])
            f.close()

    @classmethod
    def _get_current_system(cls):
        return platform.system()


if __name__ == '__main__':
    # FileUtil.exist_file(path="D:\\workspace_pycharm\\config\\conf\\test.txt")
    FileUtil.get_file(path="D:/workspace_pycharm/config/conf/test.txt")
    # logging.info(platform.architecture())
    # logging.info(platform.system())
    # logging.info(platform.version())
    # logging.info(platform.platform())
    # logging.info(type(platform.architecture()))
