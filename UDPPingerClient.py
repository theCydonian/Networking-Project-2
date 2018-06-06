# UDPPingerClient.py
import time
from socket import *

serverName = str(input('input server address:\n'))
serverPort = int(input('input server port:\n'))
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
	message = "ping " + str(i) + " " + time.asctime()
	try:
		time1 = time.time()
		clientSocket.sendto(message.encode(), (serverName, serverPort))
		responseMessage, serverAddress = clientSocket.recvfrom(1024)

		print("Reply from " + serverAddress[0] + ": " + responseMessage.decode())
		print("RTT: " + str(time.time()-time1))
	except:
		print('Request timed out')
clientSocket.close()