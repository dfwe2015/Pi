# -*- coding: utf-8 -*-

import pi.commands
import pi.csv_match
from pi import modify_ip
import commands

print(modify_ip.getip())
r = pi.pi_csvRow.Row()
gatewayaddress = r.getRow()
print(gatewayaddress)
print pi.pi_commands.getstatusoutput("ping %s " % gatewayaddress[2])
# print pi_commands.getstatusoutput("ping -q -c 2 -r %s " % gatewayaddress[2])
