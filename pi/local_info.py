# -*- coding: gbk -*-

"""����������״̬"""

import socket


def get_local_ip():
    """ʹ��socket��ȡ����IP��ַ"""
    # ����ʹ�� LocalIP = socket.gethostbyname(socket.gethostname())
    # ���������õ���IPֻ��һ�����Զ�������IP��ַ�޽⣬���ַ���,�����б�
    local_ip = socket.gethostbyname_ex(socket.gethostname())
    return local_ip[2][0]  # ֻȡ�˵�һ����ַ
