#!/usr/bin/python
__author__ = "Seamus"

import socket
import re
import argparse

parser = argparse.ArgumentParser(description = "Grabs banners from server")
parser.add_argument('-s', type=str, help="The website to grab")
args = parser.parse_args()


host = args.s

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, 80))

http_get = "GET / HTTP/1.1\nHOST: "
new = "\n\n"
request = http_get+host+new
r=request.encode('ascii')
data = ''
try:
	socket.sendall(r)
	data = socket.recvfrom(1024)
finally:
	print("Connection closing")
	socket.close()

strdata = data[0].decode("utf-8")
print(strdata)

