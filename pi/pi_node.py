# -*- coding: utf-8 -*-

import pi_getIP
import pi_csvRow
import pi_commands

class Node(object):
    node_count = 0

    def __init__(self, node_ip):
        self.node_ip = node_ip
        self.state = pi_commands.getstatusoutput("ping %s" % self.node_ip)
        # self.state = pi_commands.getstatusoutput("ping -q -c 2 -r %s" % self.node_ip)
        Node.node_count += 1
        print("Node类第 %s 次被实现" % Node.node_count)

    def getNodeIP(self):
        return self.node_ip

    def getState(self):
        return self.state

# # n = Node('1.1.1.1')
# n = Node(pi_getIP.getip())
# print(Node.nodecode)
# print n.getState()


class Map(object):

    def __init__(self, start_ip):
        self.r = pi_csvRow.Row()
        self.node = Node(start_ip)
        self.row_list_num = 1
        if self.r.getRow():
            for i in self.r.getRow()[2:]:
                if i:
                    self.node = Node(i)
                    self.row_list_num += 1
                else:
                    break

                if self.node.getState()[0]:
                    print("发现不可达地址: %s" % self.node.getNodeIP())
                    break
        print("最终地址 %s 可达" % self.node.getNodeIP())

    def getFirstRow(self):
        return self.r.getFirstRow()

    def getRowListNo(self):
        return self.row_list_num

    def getNode(self):
        return self.node



m = Map(pi_getIP.getip())
print("=" * 50)
print("node节点停在第 %r 列" % m.getRowListNo())
print("得到Node实例：%r" % m.getNode())
print("node节点的IP：%r" % m.getNode().getNodeIP())
print("node节点的状态反馈：%r" % m.getNode().getState()[1])
print("csv文件第一行第 %r 列内容：%r" % (m.getRowListNo(), m.getFirstRow()[m.getRowListNo()]))
