# -*- coding: utf-8 -*-
# @Time     : 2018/3/3 20:44
# @Author   : ice
# @File     : zookeeper_engine.py
# @Software : PyCharm
from __future__ import unicode_literals

import logging

from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError

from myconf.engine.engine import AbstractEngine
from myconf.path import CONFIG_PATH_ORDER_LIST
from myconf.utils.config_util import ConfigUtil


class ZookeeperEngine(AbstractEngine):
    """
    Zookeeper连接引擎管理类
    """

    def __init__(self, **kwargs):
        """
        Zookeeper连接引擎参数
        :param hosts:
        :param timeout:
        """
        hosts = kwargs.get("hosts", None)
        time_out = kwargs.get("timeout", 10.1)

        cp = ConfigUtil.get_config_parser()
        if not hosts:
            hosts = cp.get(section="zookeeper", option="hosts")
        self._zk = KazooClient(
            hosts=hosts,
            timeout=time_out,
        )

    def connect(self):
        self._zk.start()
        children = self._zk.get_children(path='/')
        print(children)
        logging.info('Zookeeper连接成功')

    def get_all_config(self):
        path = self._get_path()
        return self._zk.get(path=path)

    def get_static_config(self, config_host="project", config_type="dev", config_version="1"):
        path = self._get_path(
            config_type=config_type,
            config_version=config_version,
        )

    def get_config_by_key(self, **kwargs):
        if "config_host" not in kwargs:
            kwargs.update({"config_host": "mersea"})
        if "config_purpose" not in kwargs:
            kwargs.update({"config_purpose": "dev"})
        if "config_personal" not in kwargs:
            kwargs.update({"config_personal": None})
        if "config_personal" not in kwargs:
            kwargs.update({"config_version": "1"})
        if "config_type" not in kwargs:
            kwargs.update({"config_type": "static"})

        path = self._get_path(**kwargs)
        config = None
        try:
            config = self._zk.get(path=path)
        except NoNodeError as e:
            logging.warn("%s")

        return config

    def _get_path(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        path = "/config"
        path += "/"
        for k in CONFIG_PATH_ORDER_LIST:
            v = kwargs.get(k, None)
            if v:
                path += v
                path += "/"

        logging.info(path)
        return path
