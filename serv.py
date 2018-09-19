import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = "localhost"   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

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