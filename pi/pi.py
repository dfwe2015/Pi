# -*- coding: utf-8 -*-

import pi_commands
import pi_csvRow

gatewayaddress = pi_csvRow.getRow()
# print pi_commands.getstatusoutput("ping %s " % gatewayaddress[2])
print pi_commands.getstatusoutput("ping -q -c 2 -r %s " % gatewayaddress[2])
