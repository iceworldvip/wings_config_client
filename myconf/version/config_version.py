# -*- coding: utf-8 -*-
# @Time     : 2018/2/10 23:37
# @Author   : ice
# @File     : version.py
# @Software : PyCharm
from __future__ import unicode_literals

from typedecorator import params


class ConfigVersion(object):
    """
    版本
    """

    @params(self={object}, config_version={int, long})
    def __init__(
            self,
            config_version=1):
        """
        配置版本
        :param config_version: 配置版本
        """
        self.config_version = config_version

    def _generate(self):
        """
        生成version
        :return:
        """
        if self.config_version:
            self.config_version += 1
        else:
            self.config_version = 1

    def get_default_version(self):
        return self.config_version
