#!/usr/bin/env python 
import socket
import os
import sys
user=raw_input("Name: ");
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
	data = s.recv(1024)
	clear()
	print "\n".join(data.split(";;;"))
	message = raw_input('message:')
	s.send(user+": "+message)
s.close()