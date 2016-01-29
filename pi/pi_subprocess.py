# -*- coding: utf-8 -*-

"""引用网上的一个例子，了解一下subprocess。
http://blog.csdn.net/xanxus46/article/details/44682073
    搜了一天，竟然没找到一段合适的代码来获取机器中所有网卡的ip，
掩码和广播地址，大部分都是用socket，但是socket通常返回的要不就
是内网地址，要不就是公网地址，不能够找到所有地址，真的太忧桑了，
决定自己通过ifconfig或ipconfig的返回信息，一步步地过滤了。这次
的代码主要用到了正则表达式和subprocess模块，而且为了兼容所有平台
（win，linux和mac），也用到了platform来判断系统类型，不说太多，
代码如下："""

import subprocess
import re
import platform
import os


def find_all_ip(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile('(inet %s)' % ipstr)
        if platform == "Linux":
            ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return iplist
    elif platform == "Windows":
        # os.popen('CHCP 437')
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        # print(ipconfig_process)
        output = ipconfig_process.stdout.read()
        print(output)
        ip_pattern = re.compile("IPv4 Address(\. )*: %s" % ipstr)
        # print(ip_pattern)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return iplist


def find_all_mask(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    maskstr = '0x([0-9a-f]{8})'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_pattern = re.compile('(netmask %s)' % maskstr)
        pattern = re.compile(maskstr)
        if platform == "Linux":
            mask_pattern = re.compile(r'Mask:%s' % ipstr)
            pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '0xff000000' and mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        return masklist
    elif platform == "Windows":
        # os.popen('CHCP 437')
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_pattern = re.compile(r"Subnet Mask (\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        return masklist


def get_broad_addr(ipstr, maskstr):
    iptokens = map(int, ipstr.split("."))
    masktokens = map(int, maskstr.split("."))
    broadlist = []
    for i in range(len(iptokens)):
        ip = iptokens[i]
        mask = masktokens[i]
        broad = ip & mask | (~mask & 255)
        broadlist.append(broad)
    return '.'.join(map(str, broadlist))


def find_all_broad(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = (ipconfig_process.stdout.read())
        broad_pattern = re.compile('(broadcast %s)' % ipstr)
        if platform == "Linux":
            broad_pattern = re.compile(r'Bcast:%s' % ipstr)
        pattern = re.compile(ipstr)
        broadlist = []
        for broadaddr in broad_pattern.finditer(str(output)):
            broad = pattern.search(broadaddr.group())
            broadlist.append(broad.group())
        return broadlist
    elif platform == "Windows":
        # os.system('CHCP 437')
        # subprocess.Popen('CHCP 437', shell=True)
        iplist = find_all_ip(platform)
        masklist = find_all_mask(platform)
        broadlist = []
        for i in range(len(iplist)):
            broadlist.append(get_broad_addr(iplist[i], masklist[i]))
        return broadlist


system = platform.system()
# print(system)
if system == "Windows":
    os.popen('CHCP 437')
#     subprocess.Popen('CHCP 437', shell=True)
print(find_all_ip(system))
# print(find_all_mask(system))
# print(find_all_broad(system))
