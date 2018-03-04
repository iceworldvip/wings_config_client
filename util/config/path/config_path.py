# -*- coding: utf-8 -*-
# @Time     : 2018/2/11 8:36
# @Author   : ice
# @File     : config_path.py
# @Software : PyCharm
from __future__ import unicode_literals

from enum import Enum


class ConfigPath(Enum):
    """
    配置路径
    """
    root = 'config'
    host = 'default'
    static = 'static'
    dynamic = 'dynamic'
    version = 'version'
