# -*- coding: utf-8 -*-
# @Time     : 2018/2/10 23:32
# @Author   : ice
# @File     : config_manager.py
# @Software : PyCharm
from __future__ import unicode_literals

from myconf.engine.engine import AbstractEngine


class ConfigManager(object):
    """
    配置管理器
    """

    def __init__(
            self,
            engine=AbstractEngine,
            **kwargs
    ):
        """
        配置管理器初始化值
        :param hosts:
        :param config_type:
        :param version:
        """
        self.engine = engine(**kwargs)

    def get_config(
            self,
            config_host="mersea",
            config_type='dev',
            config_version=None,
            **kwargs):
        self.engine.connect()
        config_data = self.engine.get_config_by_key(
            config_host=config_host,
            config_type=config_type,
            config_version=str(config_version),
            **kwargs
        )
        return config_data
