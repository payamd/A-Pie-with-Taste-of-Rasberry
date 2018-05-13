

import socket
import sys

# create a socket object

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostbyname("192.168.1.200")
port = 1234
print("msg sent successfully ")

# connection to hostname on the port.
ms.connect((host, port))
print(host, port)

while True:
    msg = input("What's your message? ")
    message = msg
    ms.sendall(message.encode('utf-8'))
    if msg == 'finish':
         break


ms.close()

# print (data.decode('ascii'))