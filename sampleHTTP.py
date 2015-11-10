#!/usr/bin/python
__author__ = "Seamus"

import http.client

http = http.client.HTTPConnection("www.google.com")
http.request("GET", "/")

data = http.getresponse()
print(data.code)
print(data.headers)
text = data.readlines()
for t in text:
	print(t.decode('utf-8'))

