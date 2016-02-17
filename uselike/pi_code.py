# -*- coding: utf-8 -*-

import commands
import os
import socket

import pi.commands

# 使用socket获取本机IP地址
hostname = socket.gethostname()
IPinfo = socket.gethostbyname_ex(hostname)
print(IPinfo)

# IPinfo[2]为只有一个字符串元素的列表，应加判断，如果有多个元素，则该设备有多个IP。
# 将所得元组中的列表转换为字符串
LocalIP = ''.join(IPinfo[2])
print(LocalIP)

# 将字符串分割成序列（列表）
LocalIpList = LocalIP.split('.')
print(LocalIpList)

# 如果操作系统为Windows系统，则更改活动代码页Active code page 为437 英文。936 （ANSI/OEM - 简体中文 GBK）。
if os.name == 'nt':
    os.system('CHCP 437')
    # ipconfig = os.popen('ipconfig')
    print(pi.pi_commands.getstatusoutput('ipconfig'))
    # print sys.builtin_module_names
else:
    print('不是Windows系统，那就是UNIX(POSIX)了。')
    # ipconfig = os.popen('ifconfig')
    print(commands.getstatusoutput('ifconfig'))
    # break

# text = ipconfig.read()
# sts =  ipconfig.close()#只能执行一次
# if sts is None: sts = 0
# print(text)
# print(sts)

### The end
