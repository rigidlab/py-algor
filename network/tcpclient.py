from socket import socket,AF_INET, SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',20000))
for i in range(0,10):
    s.send(b'hello')
    print(s.recv(8192))
