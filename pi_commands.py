# -*- coding: utf-8 -*-

import os, socket

#使用socket获取本机IP地址
hostname = socket.gethostname()
IPinfo = socket.gethostbyname_ex(hostname)
# LocalIP = IPinfo[2]
#将所得列表转换为字符串
LocalIP = ''.join(IPinfo[2])
# print(LocalIP)

# 如果操作系统为Windows系统，则更改活动代码页Active code page 为437 英文。936 （ANSI/OEM - 简体中文 GBK）。
if os.name == 'nt':
    os.system('CHCP 437')
    ipconfig = os.popen('ipconfig')
else:
    print('不是Windows系统，那就是POSIX了。')
    ipconfig = os.popen('ifconfig')
    # break

text = ipconfig.read()
sts =  ipconfig.close()#只能执行一次
if sts is None: sts = 0
print(text)
print(sts)

### The end

