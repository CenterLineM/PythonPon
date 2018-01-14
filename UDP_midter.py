# -*- coding: utf-8 -*-
import socket
import time
import random


UDP_IP = "192.168.43.48"#PI

UDP_PORT = 10000
IP = "192.168.43.250" #PC
PORT = 10001
print " Game Start"
random_number = random.randint(0,100)
print random_number


def f(x):
	return {
	
	}[x]

i=1
while i < 6:

	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind((UDP_IP,UDP_PORT))
	realcount = ""
	data = sock.recvfrom(1024) # buffer size is 1024 bytes
	print data
	str1 = (str(data).split("'"))[1]
	print str1
	
	#str2 = str1.split("_")
	#print str2
	#icount = len(str2)
	#print icount
	dataint = int(str1)

	print i 
	if(dataint == random_number):
		str3= "You Win !"
		sock.sendto( str3,(IP,PORT))
		print str3
		break
	elif (dataint < random_number):
		str1= "You guess number is too little, try again ! "
		sock.sendto( str1,(IP,PORT))
		print str1
		i+=1
	elif ( dataint > random_number):
		str4= " You guess number is too big , try again ! "
		sock.sendto( str4,(IP,PORT))
		print str4
		i+=1
	if(i>6):
		str5= (" You are game over ");
		sock.sendto( str5,(IP,PORT))
		print str5
		break 
		
print("Game End")

