import socket

port = 50000
s = socket.socket()
host = "localhost"
s.bind((host, port))
s.listen(5)

print('Listening....')


while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    filename='cyber.mp4'
    f = open(filename,'rb')
    l = f.read(1048576)
    while (l):
       conn.send(l)
       l = f.read(1048576)
    f.close()
    print('Done sending')
    conn.close()