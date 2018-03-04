# -*- coding: utf-8 -*-
# @Time     : 2018/2/11 0:09
# @Author   : ice
# @File     : config_type.py
# @Software : PyCharm
from __future__ import unicode_literals

from enum import Enum, unique


@unique
class ConfigType(Enum):
    """
    配置类型
    """
    dev = 'dev'
    test = 'test'
    online = 'online'
