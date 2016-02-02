# -*- coding: utf-8 -*-

import pi_commands
import pi_getaddress

gatewayaddress = pi_getaddress.getGatewayAddress()
print pi_commands.getstatusoutput("ping %s " % gatewayaddress)