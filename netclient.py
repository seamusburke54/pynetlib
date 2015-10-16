#!/bin/bash/python
__author__ = "Seamus"

import socket

host = 'localhost'

testsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address=(host,5555)
testsocket.connect(address)

try:
	msg=b"test socket\n"
	testsocket.sendall(msg)
except socket.errno as e:
       print("Socket error", e)
finally:
	testsocket.close()


