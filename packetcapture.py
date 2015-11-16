#!/usr/bin/python

__author__ = "Seamus"

import pcapy
from struct import *

devices = pcapy.findalldevs()
print(devices)


def packcap(interface, packet_size, promiscous_mode, timeout)
#device, # of byte to capture, promiscious mode, timeout
	capture = pcapy.open_live("eth0", 65536, 1, 0)
	count = 1
	while count:
		(header,payload) = capture.next()
		print(count)
		count = count + 1
	
def headunpack
	capture = pcapy.open_live("eth0", 65535, 1, 0)
	while 1:
		(header, payload) = cap.next()
		lay2hdr = payload[:14]
		lay2data = unpack("!6s6sH", lay2hdr)
		srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(lay2hdr[0]), ord(lay2hdr[1]), ord(lay2hdr[2]), ord(lay2hdr[3], ord(lay2hdr[4], ord(lay2hdr[5])
		destmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(lay2hdr[6]), ord(lay2hdr[7]), ord(lay2hdr[8]), ord(lay2hdr[9], ord(lay2hdr[10], ord(lay2hdr[11])
		print("Source Mac: ", srcmac, " Destination MAC: ". destmac)
		ipheader = unpack('!BBHHHBBH4s4s' , payload[13:34])
		timetolive = ipheader[5]
		protocol = ipheader[6]
		print("Protocol ", str(protocol), "Time to live ", str(timetolive))

def parsepcap
	pcap_file = pcapy.open_offlin("file.pcap")
	count = 1
	while count:
		print("Packet # ", count)
		count = count + 1
		(header, payload) = pacp_file.next()
		lay2hdr = payload[:14]
		lay2data = unpack("!6s6sH", lay2hdr)
		srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(lay2hdr[0]), ord(lay2hdr[1]), ord(lay2hdr[2]), ord(lay2hdr[3], ord(lay2hdr[4], ord(lay2hdr[5])
		destmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(lay2hdr[6]), ord(lay2hdr[7]), ord(lay2hdr[8]), ord(lay2hdr[9], ord(lay2hdr[10], ord(lay2hdr[11])
		print("Source Mac: ", srcmac, " Destination MAC: ". destmac)
		ipheader = unpack('!BBHHHBBH4s4s' , payload[13:34])
                timetolive = ipheader[5]
                protocol = ipheader[6]
                print("Protocol ", str(protocol), "Time to live ", str(timetolive))

