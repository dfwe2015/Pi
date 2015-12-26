# -*- coding: utf-8 -*-

import os
import socket
import commands
import pi_commands
import subprocess

#当前使用的操作系统平台
# print(os.name)
#当前工作目录
# print(os.getcwd())
#列出当前工作目录内容,放到列表中
# print(os.listdir(os.getcwd()))

# print(os.remove())

# #使用socket获取本机IP地址
# hostname = socket.gethostname()
# IPinfo = socket.gethostbyname_ex(hostname)
# print(IPinfo)
# LocalIP = IPinfo[2]
# # print(LocalIP)
# #将列表转换为字符串
# LocalIP = ''.join(LocalIP)
# # print LocalIP

#更改活动代码页Active code page 。437 英文，936 （ANSI/OEM - 简体中文 GBK）。
os.system('CHCP 437')
# os.system('CHCP 936')

# # os.system('route print')
# # os.system('ipconfig /all')
# # ipconfig = os.system('ipconfig')
# ipconfig = os.popen('ipconfig')
# print('*'*40)
# print(ipconfig.read())
# print(ipconfig.close())#如果ipcoifig命令执行成功，则返回None。

# print commands.getstatusoutput('dir')#看源码，# NB This only works (and is only relevant) for UNIX.
# print pi_commands.getstatusoutput('ping -n 1 192.168.1')
# print pi_commands.getstatusoutput('ping -n 1 192.168.1.0')
print pi_commands.getstatusoutput('ping -n 1 192.168.1.1')[0]
print pi_commands.getstatusoutput('ping -n 1 192.168.1.1')[1]
print('*'*30)
# print('*'*30)
# print(pi_commands.getstatus('ipconfig'))
# print('*'*30)
# subprocess.check_output('ipconfig','-all')

# address = LocalIP
# address = 'a'
# address = raw_input('请输入目的地址：')
# print os.system('ping '+address)
# print os.system('tracert '+address)
# os.system('tracert '+address)



