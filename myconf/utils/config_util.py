# -*- coding: utf-8 -*-
# @Time     : 2018/4/27 6:45
# @Author   : ice
# @File     : config_util.py
# @Software : PyCharm
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys

from project_path import PROJECT_PATH

# 加载配置解析器，兼容2.x与3.x版本

python_version = sys.version_info.major

if python_version == 2:
    from configparser import ConfigParser
elif python_version == 3:
    from ConfigParser import ConfigParser


class ConfigUtil(object):

    @classmethod
    def get_config_parser(cls, path=None):
        """
        获取配置对象
        :param path:
        :return:如果配置地址无法读取配置文件，返回None
        """
        cp = ConfigParser()
        file_path = (PROJECT_PATH + os.path.sep + "conf" + os.path.sep + "config.ini")
        if isinstance(path, (list, tuple, set)):
            file_path = path
        parser_result = cp.read(filenames=[file_path])
        if parser_result:
            return cp
        return None
