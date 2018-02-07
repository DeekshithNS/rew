import socket
import sys
import serial 
import time

ard = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)
 
HOST = '192.168.43.80'
PORT = 9999
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'socket created'
 

try:
	s.bind((HOST, PORT))
except socket.error as err:
	print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
	sys.exit()
 
print 'Socket Bind Success!'
 
 
s.listen(10)
print 'Socket is now listening'
 
 
while 1:
	conn, addr = s.accept()
	
	buf = conn.recv(64)
	ard.write(buf)
s.close()
