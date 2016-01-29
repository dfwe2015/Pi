# -*- coding: utf-8 -*-

import pi_commands

gateway_address_by_list = pi_commands.getipbylist()
gateway_address_by_list[3] = '1'
#修改列表格式的IP地址，比如['192', '168', '1', '66']
# 最后‘66’改为‘1’，得到['192', '168', '1', '1']一般就是默认网关。
print(gateway_address_by_list)

print(pi_commands.getipbylist())
LocalIP = '.'.join(pi_commands.getipbylist())#把列表用'.'拼接，得到IP地址字符串。
print(LocalIP)
if LocalIP == pi_commands.getip():
    print(pi_commands.getstatusoutput("ping " + pi_commands.getip()))

### The end

