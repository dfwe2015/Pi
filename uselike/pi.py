# -*- coding: utf-8 -*-

import pi.pi_commands
import pi.pi_csvRow
from pi import pi_modifyIP

print(pi_modifyIP.getip())
r = pi.pi_csvRow.Row()
gatewayaddress = r.getRow()
print(gatewayaddress)
print pi.pi_commands.getstatusoutput("ping %s " % gatewayaddress[2])
# print pi_commands.getstatusoutput("ping -q -c 2 -r %s " % gatewayaddress[2])
