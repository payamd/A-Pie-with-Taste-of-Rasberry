# import socket
# import sys
# mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host=socket.gethostbyname("www.google.com")
# try:
#     mysocket.Connect(host, 80)
# except:
#     print("cant handle that! ")
# message = "GET / HTTP/1.1\r\n\r\n"
# mysocket.sendall(message)
# data = mysocket.recv(1000)
# print (data)
# mysocket.close()


import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostbyname("www.google.com")

port = 80

# connection to hostname on the port.
s.connect((host, port))


message = 'GET / HTTP/1.0\r\n\r\n'
s.sendto(message.encode(),(host, port))


# Receive no more than 1024 bytes
data = s.recv(1024)

s.close()

print (data.decode('ascii'))