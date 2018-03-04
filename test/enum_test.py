# -*- coding: utf-8 -*-
# @Time     : 2018/2/11 0:57
# @Author   : ice
# @File     : enum_test.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

from util.config.config_manager import ConfigManager
from util.config.type.config_type import ConfigType


class EnumTest(TestCase):

    @staticmethod
    def testMethod():
        config_manager = ConfigManager(
            hosts='192.168.1.107:2181',
            config_type=ConfigType.dev,
        )
        config_manager.get_config()
