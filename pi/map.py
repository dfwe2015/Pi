# -*- coding: gbk -*-

"""���� Node �� csv"""

import network_node
import csv_match
import local_info

class Map(object):
    """���� Node �� csv"""
    def __init__(self, start_ip):

        # TODO:��һ���жϱ������
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
                if self.node.get_state()[0]:  # �ɴ�Ϊ0, ���ɴ�Ϊ1.
                    print("���ֲ��ɴ��ַ: %s" % self.node.get_node_ip())
                    break
        else:
            print("IP ��ַû���� csv �ļ���ƥ��.")
        print("���յ�ַ: %s " % self.node.get_node_ip())

    def get_node(self):
        return self.node

    def get_csv_match(self):
        return self.csv

    def get_column_num(self):
        return self.column_num


# m = Map(local_info.get_local_ip())
# print("=" * 50)
# print("�õ�Nodeʵ����%r" % m.get_node())
# print("node�ڵ��IP��%r" % m.get_node().get_node_ip())
# print("node�ڵ��״̬������%r" % m.get_node().get_state()[0])
# print("node�ڵ��״̬������%r" % m.get_node().get_state()[1])
# print("node�ڵ�ͣ�ڵ� %r ��" % m.get_column_num())
# sstr = "csv�ļ���һ�е� %s �����ݣ�%s" % (m.get_column_num(), m.get_csv_match().get_csv_title()[m.get_column_num()])
# print(sstr)
# print(sstr.decode('utf-8').encode('gbk'))
#
#
# s = "���"
# print isinstance(s, unicode)
# print(s.decode('utf-8').encode('gbk'))
# print(s)
