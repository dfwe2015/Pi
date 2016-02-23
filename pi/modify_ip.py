# -*- coding: gbk -*-

"""转换IP字符串,比较（匹配）字符串"""


def compare_ip(ip_list, ip_str):
    if ip2int(ip_list[0]) <= ip2int(ip_str) <= ip2int(ip_list[1]):
        return ip_list


def ip2list(ip_str):
    """将IP字符串分割成序列（列表）并返回"""
    return ip_str.split('.')


def ip2int(ip_str):
    """将IP字符串转进行位运算,得到一个int值"""
    ip2int_list = [int(i) for i in ip_str.split('.')]
    # 将字符串转换成列表，形如[192, 168, 1, 33]。
    ip_int_code = (ip2int_list[0] << 24) | (ip2int_list[1] << 16) | (ip2int_list[2] << 8) | ip2int_list[3]
    # 进行位运算得到一个int数值，应该可以提升效率，直接用列表进行比较也是可以的。
    # 位运算，左移8位，相当于乘以256.
    # ip_code = (l[0] * 1000000000) + (l[1] * 1000000) + (l[2] * 1000) + l[3]
    return ip_int_code



