#! /usr/bin/env python

## Copyright (C) 2012 - 2020 ENCRYPTED SUPPORT LP <adrelanos@riseup.net>
## See the file COPYING for copying conditions.

import sys
from scapy.all import *

#define the target gateway & data payload
target = "scanme.nmap.org"
#target = "45.33.32.156"

data = "testing"

#define packets
ip = IP()
tcp = TCP()

#define packet parameters
ip.dst = target

#loop through all TCP ports
for tcp_port in range(0,65535):
        tcp.dport = tcp_port
        send(ip/tcp/data)
