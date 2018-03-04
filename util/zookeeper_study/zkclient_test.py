# -*- coding: utf-8 -*-
# @Time     : 2018/2/2 0:57
# @Author   : ice
# @File     : zkclient_test.py
# @Software : PyCharm
from __future__ import unicode_literals

from kazoo.client import KazooClient

# 获取zookeeper客户端
# zk = KazooClient(hosts='192.168.31.99:2181')
# zk = KazooClient(hosts='192.168.1.100:2181')
zk = KazooClient(hosts='192.168.1.111:2181')


@zk.add_listener
def test(state):
    print(state)


if __name__ == '__main__':
    zk.start()
    with open("./__init__.py", mode="rb") as f:
        lines = f.readlines()
        b = b''
        for line in lines:
            b += bytes(line)
        zk.create(
            path="/test",
            value=b,
            ephemeral=False,
        )
        data, stat = zk.get(
            path="/test",
            watch=test
        )
        exec(b"{data}".format(data=data))

    # zk_clients = []
    # for i in xrange(1000):
    #     zk = KazooClient(hosts='192.168.31.99:2181')
    #     zk.start(100)
    #     zk_clients.append(zk)
    #
    # print(10)
