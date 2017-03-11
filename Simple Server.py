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
        while True:
            data = conn.recv(5000)
            data = data.decode('utf-8')

            if data == 'finish':
                print('connection finish')
                conn.close()
                ms.close()
                print('Server close')
            else:
                if data == 'roshan':
                    print('Roshaaaaan!!!')
                if data == 'khamoosh':
                    print('khamoooosh!!!')
                else:
                    print(data)


