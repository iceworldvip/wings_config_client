# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 20:03
# @Author   : ice
# @File     : engine.py
# @Software : PyCharm
from abc import ABCMeta, abstractmethod


class AbstractEngine(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        """
        实现连接方法
        :return:
        """
        return NotImplemented

    @abstractmethod
    def get_static_config(self):
        """
        获取静态配置
        :return:
        """
        return NotImplemented

    @abstractmethod
    def get_config_by_key(self, config_host, config_type, config_version, **kwargs):
        """
        获取配置
        :return:
        """
        return NotImplemented
