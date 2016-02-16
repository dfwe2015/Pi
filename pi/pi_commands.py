# -*- coding: utf-8 -*-

"""重写(修改)了commands.py,解决调用系统cmd的需求。
def getstatusoutput(cmd)返回一个元组,[0]=0表示调用成功，
[0]=其它(一般为1)表示调用失败，[1]为cmd返回的内容"""

import subprocess
import os
import platform


def getstatus(cmd):
    return getstatusoutput(cmd)[0]


def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    return getstatusoutput(cmd)[1]


def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    # if os.name == 'nt':
    # if sys.platform == "Windows":
    if platform.system() == "Windows":
        """ 如果操作系统为Windows系统，则更改活动代码页Active code page 为437 英文。
        如果为936,则是(ANSI/OEM - 简体中文 GBK）。"""
        # os.system('CHCP 437')
        os.popen('CHCP 437')
        # subprocess.Popen('CHCP 437', shell=True)
        # subprocess无法达到更改Windows默认代码页的目的，暂时放弃。

    pipe = os.popen(cmd)
    text = pipe.read()
    sts = pipe.close() # 命令执行成功, 得到None
    # pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    # text = pipe.stdout.read()
    # sts = pipe.stdout.close()

    if sts is None:
        sts = 0  # 成功, 返回0

    if text[-1:] == '\n':
        text = text[:-1]  # 去掉text结尾的回车符。

    return sts, text
