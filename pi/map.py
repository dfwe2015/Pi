# -*- coding: gbk -*-

"""适配 Node 和 csv"""

import network_node
import csv_match
import local_info

class Map(object):
    """适配 Node 和 csv"""
    def __init__(self, start_ip):

        # TODO:进一步判断本机情况
        if not start_ip:
            pass
        elif start_ip == '127.0.0.1':
            pass

        self.node = network_node.NetworkNode(start_ip)
        self.csv = csv_match.CsvMatch(start_ip)
        self.column_num = 1
        if self.csv.get_csv_row():
            for address in self.csv.get_csv_row()[2:]:
                if address:
                    self.node = network_node.NetworkNode(address)
                    self.column_num += 1
                else:
                    break
                if self.node.get_state()[0]:  # 可达为0, 不可达为1.
                    print("发现不可达地址: %s" % self.node.get_node_ip())
                    break
        else:
            print("IP 地址没有在 csv 文件中匹配.")
        print("最终地址: %s " % self.node.get_node_ip())

    def get_node(self):
        return self.node

    def get_csv_match(self):
        return self.csv

    def get_column_num(self):
        return self.column_num


# m = Map(local_info.get_local_ip())
# print("=" * 50)
# print("得到Node实例：%r" % m.get_node())
# print("node节点的IP：%r" % m.get_node().get_node_ip())
# print("node节点的状态反馈：%r" % m.get_node().get_state()[0])
# print("node节点的状态反馈：%r" % m.get_node().get_state()[1])
# print("node节点停在第 %r 列" % m.get_column_num())
# sstr = "csv文件第一行第 %s 列内容：%s" % (m.get_column_num(), m.get_csv_match().get_csv_title()[m.get_column_num()])
# print(sstr)
# print(sstr.decode('utf-8').encode('gbk'))
#
#
# s = "你好"
# print isinstance(s, unicode)
# print(s.decode('utf-8').encode('gbk'))
# print(s)
