# -*- coding: utf-8 -*-

import pi_commands


ass = pi_commands.get_ip_list()
gateway_address = ass[:]
gateway_address[3] = '1'
#修改列表格式的IP地址，比如['192', '168', '1', '66']
# 最后‘66’改为‘1’，得到['192', '168', '1', '1']一般就是默认网关。
print(gateway_address)
print(ass)

ppp = '.'.join(gateway_address)#把列表用'.'拼接，得到IP地址字符串。
print(ppp)
print(pi_commands.get_status_output("ping " + ppp))
print(pi_commands.get_status_output("ping " + pi_commands.get_ip()))

### The end

