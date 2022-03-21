from socketserver import *

host = 'localhost'
port = 450
addr = (host, port)

class TCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('server recieved: '+str(self.data))

        self.request.sendall(b'Hello!')

if __name__ == '__main__':
    server = TCPServer(addr, TCPHandler)
    print('Server start')
    server.serve_forever()
