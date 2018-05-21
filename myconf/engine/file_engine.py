# -*- coding: utf-8 -*-
# @Time     : 2018/5/19 22:56
# @Author   : ice
# @File     : file_engine.py
# @Software : PyCharm
from __future__ import absolute_import
from __future__ import unicode_literals

from myconf.engine.engine import AbstractEngine
from project_path import PROJECT_PATH


class FileEngine(AbstractEngine):
    """

    """

    def __init__(self, file_path=PROJECT_PATH + "conf"):
        self.file_path = file_path

    def connect(self):
        """
        实现连接方法
        :return:
        """
        with open(file=self.file_path, mode="rb+") as f:
            if not f:
                raise Exception()
            print(f.name.encode())

    def get_static_config(self):
        """
        获取静态配置
        :return:
        """
        return NotImplemented

    def get_all_config(self):
        return NotImplemented

    def get_config_by_key(self, config_host, config_type, config_version, **kwargs):
        """
        获取配置
        :return:
        """
        return NotImplemented
