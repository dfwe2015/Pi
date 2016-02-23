# -*- coding: gbk -*-

"""处理本机网络状态"""

import socket


def get_local_ip():
    """使用socket获取本机IP地址"""
    # 可以使用 LocalIP = socket.gethostbyname(socket.gethostname())
    # 但是这样得到的IP只有一个，对多网卡多IP地址无解，换种方法,返回列表。
    local_ip = socket.gethostbyname_ex(socket.gethostname())
    return local_ip[2][0]  # 只取了第一个地址
