

import socket

# create a socket object
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostbyname("192.168.1.200")
port = 1234
print("msg sent successfully ")

# connection to hostname on the port.
ms.connect((host, port))


message = b"hello world!!!"
ms.sendall(message)
# ms.sendto(message.encode(),(host, port))
#
#
# # Receive no more than 1024 bytes
# data = ms.recv(1024)

ms.close()

# print (data.decode('ascii'))