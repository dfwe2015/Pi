# -*- coding: utf-8 -*-

import socket

# def getip(LocalIP=socket.gethostbyname(socket.gethostname())):
# 这样得到的IP只有一个，对多网卡多IP地址无解，换种方法,返回列表。
def getip(LocalIP=socket.gethostbyname_ex(socket.gethostname())):
    # 使用socket获取本机IP地址
    # LocalIP = socket.gethostbyname(socket.gethostname())
    #得到本地ip

    return LocalIP[2][0]


def getipbylist(ipstr=getip()):
    # 将IP字符串分割成序列（列表）并返回
    return ipstr.split('.')


def getip2int(ipstr=getip()):
    ipintlist = [int(i) for i in ipstr.split('.')]
    # 将字符串转换成列表，形如[192, 168, 1, 33]。
    ipintcode = (ipintlist[0] << 24) | (ipintlist[1] << 16) | (ipintlist[2] << 8) | ipintlist[3]
    # 进行位运算得到一个int数值，应该可以提升效率，直接用列表进行比较也是可以的。
    # 位运算，左移8位，相当于乘以256.
    # ipcode = (l[0] * 1000000000) + (l[1] * 1000000) + (l[2] * 1000) + l[3]

    return ipintcode