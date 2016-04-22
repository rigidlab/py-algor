from socket import socket, AF_INET, SOCK_DGRAM

s=socket(AF_INET, SOCK_DGRAM)

if __name__=='__main__':
    try:
        s.sendto(b'time', ('localhost',20000))
	print ('recv:', s.recvfrom(8192))
    except KeyboardInterrupt:
        s.close()	 
