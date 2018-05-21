# -*- coding: utf-8 -*-
# @Time     : 2018/4/27 6:49
# @Author   : ice
# @File     : test_config.py
# @Software : PyCharm
from __future__ import unicode_literals

import os
from ConfigParser import ConfigParser
from unittest import TestCase


class TestConfig(TestCase):
    def test_config_parser(self):
        project_dir = os.path.dirname(path=os.path.abspath(path=__file__))
        cp = ConfigParser()
        read_result = cp.read(filenames=[project_dir + '/config/config.ini'])
        print(read_result)
