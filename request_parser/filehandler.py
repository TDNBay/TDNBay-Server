import os
import struct

from db import utils


class FileRequestHandler:
    
    def __init__(self, client, parsed_data):
        self.client = client
        self.parsed_data = parsed_data
    
    def handle_request(self):
        file_id = int(self.parsed_data['detail'])
        file_name = utils.file_name_by_id(file_id)
        print("Enviando", file_name, "...")
        self.client.send(bytes([1]))
        lennbytes = struct.pack(">I", os.path.getsize(file_name))
        self.client.send(bytes([len(lennbytes)]))
        self.client.send(lennbytes)
        f = open(file_name, 'rb')
        l = f.read(16384)
        while l:
            self.client.send(l)
            l = f.read(16384)
        f.close()
        print("Envio finalizado, " + file_name)
