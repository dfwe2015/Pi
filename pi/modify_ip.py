# -*- coding: gbk -*-

"""ת��IP�ַ���,�Ƚϣ�ƥ�䣩�ַ���"""


def compare_ip(ip_list, ip_str):
    if ip2int(ip_list[0]) <= ip2int(ip_str) <= ip2int(ip_list[1]):
        return ip_list


def ip2list(ip_str):
    """��IP�ַ����ָ�����У��б�������"""
    return ip_str.split('.')


def ip2int(ip_str):
    """��IP�ַ���ת����λ����,�õ�һ��intֵ"""
    ip2int_list = [int(i) for i in ip_str.split('.')]
    # ���ַ���ת�����б�����[192, 168, 1, 33]��
    ip_int_code = (ip2int_list[0] << 24) | (ip2int_list[1] << 16) | (ip2int_list[2] << 8) | ip2int_list[3]
    # ����λ����õ�һ��int��ֵ��Ӧ�ÿ�������Ч�ʣ�ֱ�����б���бȽ�Ҳ�ǿ��Եġ�
    # λ���㣬����8λ���൱�ڳ���256.
    # ip_code = (l[0] * 1000000000) + (l[1] * 1000000) + (l[2] * 1000) + l[3]
    return ip_int_code



