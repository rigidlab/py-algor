from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and cleint socket
        msg,sock=self.request
        print('recv:',msg)
        if msg == b'time':
            resp=time.ctime()
        else:
            print('Happy Friday')
            resp='Happy Friday'
        sock.sendto(resp.encode('ascii'),self.client_address)    

if __name__=='__main__':
    serv =UDPServer(('',20000),TimeHandler)
    serv.serve_forever()

