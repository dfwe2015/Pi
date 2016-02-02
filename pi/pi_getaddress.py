# -*- coding: utf-8 -*-

import pi_csv
import pi_compare

def getGatewayAddress(rowlist=pi_csv.getrowlist()):

    for row in rowlist:
        gatewayaddress = pi_compare.compareip(row)
        if gatewayaddress:
            return gatewayaddress[2]#返回第三列，本地网关地址。

