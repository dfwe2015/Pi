# -*- coding: utf-8 -*-

import os
import socket

"""重写(修改)了commands.py,解决调用系统cmd的需求。
def getstatusoutput(cmd)返回一个元组,[0]=0表示调用成功，[0]=其它(一般为1)表示调用失败，[1]为cmd返回的内容"""

def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    return getstatusoutput(cmd)[1]

def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    if os.name == 'nt':
        """ 如果操作系统为Windows系统，则更改活动代码页Active code page 为437 英文。
        如果为936,则是(ANSI/OEM - 简体中文 GBK）。"""
        os.system('CHCP 437')

    pipe = os.popen(cmd)
    text = pipe.read()
    sts = pipe.close()

    if sts is None:
        sts = 0

    #去掉text结尾的回车符。
    if text[-1:] == '\n':
        text = text[:-1]

    return sts, text

def getip():
    # 使用socket获取本机IP地址
    LocalIP = socket.gethostbyname(socket.gethostname())#得到本地ip

    return LocalIP

def getipbylist():
    # 将字符串分割成序列（列表）
    return getip().split('.')


### The end