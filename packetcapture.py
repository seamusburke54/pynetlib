#!/usr/bin/python

__author__ = "Seamus"

import pcapy

devices = pcapy.findalldevs()
print(devices)

#device, # of byte to capture, promiscious mode, timeout
capture = pcapy.open_live("eth0", 65536, 1, 0)
count = 1
while count:
	(header,payload) = capture.next()
	print(count)
	count = count + 1
	

