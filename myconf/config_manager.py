# -*- coding: utf-8 -*-
# @Time     : 2018/2/10 23:32
# @Author   : ice
# @File     : config_manager.py
# @Software : PyCharm
from __future__ import unicode_literals

from myconf.engine.zookeeper_engine import ZookeeperEngine

"""
配置管理器
"""


class ConfigManager(object):
    """
    配置管理器
    """

    def __init__(
            self,
            engine=ZookeeperEngine,
            **kwargs
    ):
        """
        配置管理器初始化值
        :param hosts:
        :param config_type:
        :param version:
        """
        self.engine = engine(**kwargs)

    def get_config(self, **kwargs):
        """
        获取配置
        :param kwargs:
        :return:
        """
        self.engine.connect()
        config_data = self.engine.get_config_by_key(**kwargs)
        return config_data

    def get_all_config(self):
        """
        获取所有配置
        :return:
        """
        self.engine.connect()
        config_data = self.engine.get_all_config()
        return config_data
