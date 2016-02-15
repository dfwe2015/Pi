# -*- coding: utf-8 -*-
from pi.pi_compare import ip2int
import socket

# 排列ip地址列表，暂时不用的。

iplists = ['192.168.1.33','10.5.2.4','10.5.1.3','202.98.96.68','133.120.1.1','192.168.1.22']

def sort_ip(iplist):

    # 利用socket.inet_aton 转换为十进制比较
    # return sorted(iplist, key=socket.inet_aton)

    # lambda 表达式 与 split 分段排序
    # return sorted(iplist,key = lambda x: (x[0].split('.'),x.split('.')[1],x.split('.')[2],x.split('.')[3]))

    # 通过移位操作，转换十进制整数进行比较
    # sort()函数可以传入一个用于比较的函数，这个比较函数接收两个参数，返回需要返回>0, 0, <0的值，因此使用cmp就可以。
    iplist.sort(lambda x, y: cmp(ip2int(x), ip2int(y)))
    return iplist


print sort_ip(iplists)