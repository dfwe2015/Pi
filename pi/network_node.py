# -*- coding: utf-8 -*-

"""验证网络节点"""

import pi_commands


class NetworkNode(object):
    """网络节点的类, set一个IP地址, get节点状态，成功state[0]为0。"""
    node_count = 0

    def __init__(self, node_ip):
        self.node_ip = node_ip
        self.state = pi_commands.getstatusoutput("ping -n 2 %s" % self.node_ip)
        # self.state = pi_commands.getstatusoutput("ping -c 2 %s" % self.node_ip)
        NetworkNode.node_count += 1
        print("===Node类第 %s 次被实现===" % NetworkNode.node_count)
        print("commands状态码: %r" % self.state[0])
        print("commands信息:")
        print(self.state[1])
        print("\n")

    def get_node_ip(self):
        return self.node_ip

    def get_state(self):
        return self.state

