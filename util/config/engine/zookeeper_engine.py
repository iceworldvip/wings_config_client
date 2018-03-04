# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 20:44
# @Author   : ice
# @File     : zookeeper_engine.py
# @Software : PyCharm
from __future__ import unicode_literals

import logging

from kazoo.client import KazooClient

from util.config.engine.engine import AbstractEngine


class ZookeeperEngine(AbstractEngine):
    """
    Zookeeper连接引擎管理类
    """

    def __init__(self, hosts, timeout):
        """
        Zookeeper连接引擎参数
        :param hosts:
        :param timeout:
        """
        self._zk = KazooClient(
            hosts=hosts,
            timeout=timeout,
        )

    def connect(self):
        self._zk.start()
        children = self._zk.get_children(path='/')
        print(children)
        logging.info('Zookeeper连接成功')

    def get_static_config(self, config_host="project", config_type="dev", config_version="1"):
        path = self._get_path(
            config_type=config_type,
            config_version=config_version,
        )

    def get_config_by_key(self, config_host="project", config_type="dev", config_version="1", **kwargs):
        path = self._get_path(
            config_host=config_host,
            config_type=config_type,
            config_version=config_version,
            **kwargs
        )
        return self._zk.get(path=path)

    def _get_path(self, config_host, config_type, config_version, **kwargs):
        path = "/config"
        path += "/"
        path += config_host
        path += "/"
        path += config_type
        path += "/"
        path += config_version
        for item in kwargs.iterkeys():
            path_append = kwargs.get(item, "")
            if path_append:
                path += "/" + path_append

        logging.info(path)
        return path
