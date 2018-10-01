import json
import socket
import struct

port = 50000
s = socket.socket()
host = "192.168.1.161"
s.bind((host, port))
s.listen(5)

print('Listening....')



while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = []
    head = conn.recv(1)[0]
    print(head)
    if not head: #JSON
        lennn = conn.recv(1)[0]
        content_len = []
        temp = conn.recv(lennn)
        while True:
            content_len += temp
            if not len(content_len) - lennn:
                break
            temp = conn.recv(lennn)

        lenc = int.from_bytes(content_len, byteorder='big', signed=False)
        json_bytes = []
        temp = conn.recv(lenc)
        while True:
            json_bytes += temp
            if not len(json_bytes) - lenc:
                break
            temp = conn.recv(lenc)
        obj = json.loads(str(bytearray(json_bytes), "utf-8"))
        print(obj)
    conn.send(bytes([1]))
    lennbytes = struct.pack(">I", 1732821)
    conn.send(bytes([len(lennbytes)]))
    conn.send(lennbytes)
    filename='impact.mp4'
    f = open(filename,'rb')
    l = f.read(8192)
    while l:
       conn.send(l)
       l = f.read(8192)
    f.close()
    print('Done sending')
    conn.close()