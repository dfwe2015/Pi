# -*- coding: utf-8 -*-

import pi_commands
import pi_csvRow
import pi_getIP

print(pi_getIP.getip())
r = pi_csvRow.Row()
gatewayaddress = r.getRow()
print(gatewayaddress)
print pi_commands.getstatusoutput("ping %s " % gatewayaddress[2])
# print pi_commands.getstatusoutput("ping -q -c 2 -r %s " % gatewayaddress[2])
