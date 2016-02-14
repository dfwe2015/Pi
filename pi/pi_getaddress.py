# -*- coding: utf-8 -*-

import pi_csv
import pi_compare

def getGatewayAddress(rowlist=pi_csv.getrowlist()):
    global gatewayaddress
    #全局变量，生命周期长，即使再次调用方法，只要值仍然有效。
    # 如果不是全局变量，那么再次调用方法时会从rowlist未被变量过
    # 的部分开始遍历，那么就跳过应该被匹配的那一行了
    for row in rowlist:
        rowaddr = pi_compare.compareip(row)
        if rowaddr:
            gatewayaddress = rowaddr[:]

    return gatewayaddress
    #第三列是本地网关地址。

