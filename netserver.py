#!/usr/bin/python

__author__ = "Seamus"

import socket

port = 9000
size = 512
host = ''

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket.bind(host, port)
socket.listen(10)

conn, address = socket.accept()
data = conn.recv(size)
if data:
	f = open("storage.dat", address[0])
	print("connection is from: ". address[0])
	f.write(address[0])
	f.write(":")
	f.write(data.decode("utf-8"))
	f.close()
socket.close()


