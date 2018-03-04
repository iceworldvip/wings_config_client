# -*- coding: utf-8 -*-
# @Time     : 2018/2/11 0:57
# @Author   : ice
# @File     : test_enum.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

from myconf.type.config_type import ConfigType


class TestEnum(TestCase):

    def test_enum(self):
        print(ConfigType, type(ConfigType))
        print(ConfigType.dev, type(ConfigType.dev))
        print(ConfigType.dev.value, type(ConfigType.dev.value))
