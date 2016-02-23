# -*- coding: gbk -*-

"""��д(�޸�)��commands.py,�������ϵͳcmd������
def getstatusoutput(cmd)����һ��Ԫ��,[0]=0��ʾ���óɹ���
[0]=����(һ��Ϊ1)��ʾ����ʧ�ܣ�[1]Ϊcmd���ص�����"""

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
    # if platform.system() == "Windows":
    #
    #     """ �������ϵͳΪWindowsϵͳ������Ļ����ҳActive code page Ϊ437 Ӣ�ġ�
    #     936Ϊ(ANSI/OEM - �������� GBK��, 65001ΪUTF-8����"""
    #     # os.system('CHCP 437')
    #     os.popen('CHCP 65001')
    #     # subprocess.Popen('CHCP 437', shell=True)
    #     # subprocess�޷��ﵽ����WindowsĬ�ϴ���ҳ��Ŀ�ģ���ʱ������

    pipe = os.popen(cmd)
    text = pipe.read()
    text.decode('gbk').encode('gbk')
    sts = pipe.close() # ����ִ�гɹ�, �õ�None
    # pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    # text = pipe.stdout.read()
    # sts = pipe.stdout.close()

    if sts is None:
        sts = 0  # �ɹ�, ����0

    if text[-1:] == '\n':
        text = text[:-1]  # ȥ��text��β�Ļس�����

    return sts, text
