# -*- coding: utf-8 -*-
# @Time     : 2018/2/10 23:27
# @Author   : ice
# @File     : path_manager.py
# @Software : PyCharm
from __future__ import unicode_literals

from util.config.path.config_path import ConfigPath


class PathManager(object):
    """
    路径管理器
    """

    def __init__(
            self,
            host_name='',
            config_type='',
            config_version=1):
        self.path = ConfigPath.root.value
        self.host_name = host_name
        self.config_type = config_type
        self.config_version = config_version

    def get_config_path(self):
        """

        :return:
        """
        self.path += "/"
        self.path += self.host_name if self.host_name else "mersea"
        self.path += "/"
        self.path += self.get_config_type_path()
        self.path += "/"
        self.path += str(self.get_config_version_path())
        return self.path

    def get_root_path(self):
        return self.path

    def get_config_type_path(self):
        return self.config_type

    def get_config_version_path(self):
        return self.config_version

