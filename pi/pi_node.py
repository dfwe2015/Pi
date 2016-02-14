# -*- coding: utf-8 -*-

import pi_getip
import pi_csvRow
import pi_commands

class Node(object):
    nodecode = 1

    def __init__(self, node_ip):
        self.node_ip = node_ip
        self.state = pi_commands.getstatusoutput("ping -q -c 2 -r %s" % self.node_ip)
        Node.nodecode += 1

    def getNextIP(self):

        # self.state[0]值不是'0',说明没有ping通
        if self.state[0]:
            return self.state

        # 成功,获取下一节点IP
        else:
            next_ip = pi_csvRow.getRow()[Node.nodecode]
            if next_ip:
                return 0, next_ip
            else:
                return Node.nodecode, None


n = Node(pi_getip.getip())
# n = Node('1.1.1.1')
print(Node.nodecode)
print n.getNextIP()


class Map(object):
    def __init__(self, start_ip):
        self.start_ip = start_ip

    gatewayaddress = pi_csvRow.getRow()
    print(gatewayaddress)
    print(len(gatewayaddress))

    # print "length of addressline is %s " % (len(pi_getaddress.getGatewayAddress()))

    # def nextNode(self):
    #     n = Node()
    #     n.setNodeIP(pi_getip.getip())
    #     return n.getNextIP()
m = Map(pi_getip.getip())
print(m.start_ip)



