# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 7:50
# @Author   : ice
# @File     : test_path_manager.py
# @Software : PyCharm
from __future__ import unicode_literals

from unittest import TestCase

from util.config.path.config_path import ConfigPath
from util.config.path.path_manager import PathManager


class TestPathManager(TestCase):

    def test_get_config_path(self):
        path_manager = PathManager(
            host_name=ConfigPath.host.value,
            config_type='dev',
            config_version=1)
        print(path_manager.get_config_path())
