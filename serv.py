import json
import socket
import struct

port = 50000
s = socket.socket()
host = "localhost"
s.bind((host, port))
s.listen(5)

print('Listening....')



while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = []
    head = s.recv(1)[0]
    if not head: #JSON
        content_len = s.recv(s.recv(1)[0])
        lenc = struct.unpack("I", bytearray(content_len))[0]
        json_bytes = s.recv(lenc)
        obj = json.loads(json_bytes.decode("utf-8"))
        print(obj)

    filename='cyber.mp4'
    f = open(filename,'rb')
    l = f.read(1048576)
    while (l):
       conn.send(l)
       l = f.read(1048576)
    f.close()
    print('Done sending')
    conn.close()