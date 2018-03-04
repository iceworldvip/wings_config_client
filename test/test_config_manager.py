# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 10:21
# @Author   : ice
# @File     : test_config_manager.py
# @Software : PyCharm
from __future__ import unicode_literals

import logging
from unittest import TestCase

from util.config.config_manager import ConfigManager
from util.config.engine.mysql_engine import MySQLEngine
from util.config.engine.zookeeper_engine import ZookeeperEngine

logging.root.setLevel(logging.DEBUG)


class TestConfigManager(TestCase):
    def test_zookeeper_get_config(self):
        config_manager = ConfigManager(engine=ZookeeperEngine, hosts='192.168.31.18:2181', timeout=1.0)
        print(config_manager.get_config(config_host="mersea", config_type='dev', config_version=1, config_key="abc"))

    def test_mysql_get_config(self):
        config_manager = ConfigManager(engine=MySQLEngine, uri='192.168.31.18:3306')
        print(config_manager.get_config(config_type='dev', config_version=1))
