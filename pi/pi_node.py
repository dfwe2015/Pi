# -*- coding: utf-8 -*-

import pi_getip
import pi_getaddress
import pi_commands

class Node(object):
    nodecode = 1

    def __init__(self):
        Node.nodecode += 1

    def setNodeIP(self, nodeIP):
        self.nodeIP = nodeIP

    def getNextIP(self):
        if self.getState():
            return self.state
        else:
            return 0, pi_getaddress.getGatewayAddress()[Node.nodecode]

    def getState(self):
        self.state = pi_commands.getstatusoutput("ping %s" % self.nodeIP)
        return self.state[0]

n = Node()
print(Node.nodecode)
n.setNodeIP(pi_getip.getip())
# n.setNodeIP('1')
print n.getNextIP()


class Map(object):
    def __init__(self, start_ip):
        self.start_ip = start_ip

    gatewayaddress = pi_getaddress.getGatewayAddress()
    print(gatewayaddress)
    print(len(gatewayaddress))
    # print "length of addressline is %s " % (len(pi_getaddress.getGatewayAddress()))

    # def nextNode(self):
    #     n = Node()
    #     n.setNodeIP(pi_getip.getip())
    #     return n.getNextIP()
m = Map(pi_getip.getip())



