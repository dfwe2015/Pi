# -*- coding: gbk -*-

"""��֤����ڵ�"""

import pi_commands


class NetworkNode(object):
    """����ڵ����, setһ��IP��ַ, get�ڵ�״̬���ɹ�state[0]Ϊ0��"""
    node_count = 0

    def __init__(self, node_ip):
        self.node_ip = node_ip
        self.state = pi_commands.getstatusoutput("ping -n 2 %s" % self.node_ip)
        # self.state = pi_commands.getstatusoutput("ping -c 2 %s" % self.node_ip)
        NetworkNode.node_count += 1
        print("===Node��� %s �α�ʵ��===" % NetworkNode.node_count)
        print("commands״̬��: %r" % self.state[0])
        print("commands��Ϣ:")
        print(self.state[1])
        print("\n")

    def get_node_ip(self):
        return self.node_ip

    def get_state(self):
        return self.state

