# -*- coding: utf-8 -*-

import ping_ipv4
import sys

ping_ipv4.pingNode(alive=0, timeout=1, ipv6=0, number=sys.maxint, \
             node='192.168.1.1', flood=0, size=8)
