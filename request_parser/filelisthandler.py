import json
import os
import struct

from db import utils


class FileListHandler:

    def __init__(self, client, parsed_data):
        self.client = client
        self.parsed_data = parsed_data

    def handle_request(self):
        file_list = utils.files_list()
        jsonn = json.dumps(file_list)
        self.client.send(bytes([0]))
        lennbytes = struct.pack(">I", len(jsonn))
        self.client.send(bytes([len(lennbytes)]))
        self.client.send(lennbytes)
        b = bytearray()
        b.extend(jsonn.encode('utf-8'))
        self.client.send(b)