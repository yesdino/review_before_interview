import socket
import time

s = socket.socket()
s.bind(('127.0.0.1', 8888))
s.listen()

while True:
    client, addr = s.accept()
    print(client)
    timestr = time.ctime(time.time()) + '\r\n'
    client.send(timestr.encode())
    client.close()

