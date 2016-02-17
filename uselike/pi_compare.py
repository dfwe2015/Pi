# -*- coding: utf-8 -*-

import pi.modify_ip

# iplist = ['192.168.1.33','10.5.2.4','10.5.1.3','202.98.96.68','133.120.1.1','192.168.1.22']
# print compareip(iplist=['192.168.1.2', '192.168.1.254', '192.168.1.1'])
# print cmp(ip2int('192.168.1.33'), ip2int('192.168.1.36'))


# 比较IP大小，确定和哪一行csv信息匹配
def compareip(iplist, localip=pi.modify_ip.getip()):
    if pi.modify_ip.getip2int(iplist[0]) <= pi.modify_ip.getip2int(localip) <= pi.modify_ip.getip2int(iplist[1]):
        return iplist
