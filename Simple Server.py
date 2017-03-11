import socket
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
ms.bind((host, port))
ms.listen(5)
print('Server started')

while True:
    conn, addr = ms.accept()
    print('Got connection from', addr)
    conn.send(b'Thank you for connecting')
    data = conn.recv(1000)
    print(str(data))
    if not data:
        break

conn.close()
print('connection close')
ms.close()
print('Server close')