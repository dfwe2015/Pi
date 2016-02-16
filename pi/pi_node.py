# -*- coding: utf-8 -*-

"""验证网络节点"""

import pi_localInfo
import pi_csvRow
import pi_commands


class Node(object):
    """网络节点的抽象, set IP地址, get 节点状态"""
    node_count = 0

    def __init__(self, node_ip):
        self.node_ip = node_ip
        # self.state = pi_commands.getstatusoutput("ping %s" % self.node_ip)
        self.state = pi_commands.getstatusoutput("ping -c 2 %s" % self.node_ip)
        Node.node_count += 1
        print("===Node类第 %s 次被实现===" % Node.node_count)
        print("commands状态码: %r" % self.state[0])
        print("commands信息:")
        print(self.state[1])
        print("\n")

    def get_node_ip(self):
        return self.node_ip

    def get_state(self):
        return self.state


class Map(object):
    """适配 Node 和 Row, 最终返回一个 node 节点,
    同时包括 节点状态(ping通不通)/在row的第几列 等信息"""
    def __init__(self, start_ip):

        # TODO:进一步判断本机情况
        if not start_ip:
            pass
        elif start_ip == '127.0.0.1':
            pass

        self.node = Node(start_ip)
        self.row = pi_csvRow.Row(start_ip)
        self.list_num = 1
        if self.row.get_row():
            for i in self.row.get_row()[2:]:
                if i:
                    self.node = Node(i)
                    self.list_num += 1
                else:
                    break
                if self.node.get_state()[0]:  # 可达为0, 不可达为1.
                    print("发现不可达地址: %s" % self.node.get_state())
                    break
        else:
            print("IP 地址没有在 csv 文件中匹配.")
        print("最终地址: %s " % self.node.get_node_ip())

    def get_node(self):
        return self.node

    def get_row(self):
        return self.row

    def get_list_num(self):
        return self.list_num


m = Map(pi_localInfo.get_local_ip())
print("=" * 50)
print("得到Node实例：%r" % m.get_node())
print("node节点的IP：%r" % m.get_node().get_node_ip())
print("node节点的状态反馈：%r" % m.get_node().get_state()[0])
print("node节点的状态反馈：%r" % m.get_node().get_state()[1])
print("node节点停在第 %r 列" % m.get_list_num())
print("csv文件第一行第 %r 列内容：%r" % (m.get_list_num(), m.get_row().get_first_row()[m.get_list_num()]))
