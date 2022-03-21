from socketserver import *
import re

host = 'localhost'
port = 450
addr = (host, port)

def unParse(text):
    match = re.match(r'^(?P<runner_id>\d{4}) (?P<channel_id>\w{2}) (?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})\.(?P<milliseconds>\d{3}) (?P<group>\d{2})\r$', text)
    if match is None:
        raise(ValueError)
    return match.groupdict()

class TCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        recieved = self.data.decode('utf-8')
        result = unParse(recieved)
        with open('log.txt', 'a') as file:
            file.write(recieved)
        if result['group'] == '00':
            sendText = f'Спортсмен, нагрудный номер {result["runner_id"]} прошёл отсечку {result["channel_id"]} \
в {result["hours"]}:{result["minutes"]}:{result["seconds"]}.{result["milliseconds"][:1]}'.encode('utf-8')
            self.request.sendall(sendText)

if __name__ == '__main__':
    server = TCPServer(addr, TCPHandler)
    print('Server start')
    server.serve_forever()
