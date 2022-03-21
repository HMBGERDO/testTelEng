from socket import *
from telnetlib import Telnet

host = 'localhost'
port = 450
addr = (host, port)

with Telnet(host, port) as tn:
    tn.write(b'5234 15 00:02:15.120 00\r')
    print(tn.read_until(b'\n', timeout=1).decode('utf-8'))
