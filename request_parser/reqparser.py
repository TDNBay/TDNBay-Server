import json

HEADER_JSON = 0
HEADER_FILE = 1

class ParsedRequest:
    
    def __init__(self, cli):
        self.media_type = None
        self.cli = cli

    def parse(self):
        head = self.cli.recv(1)[0]
        if head == HEADER_JSON:
            lennn = self.cli.recv(1)[0]
            content_len = []
            temp = self.cli.recv(lennn)
            while True:
                content_len += temp
                if not len(content_len) - lennn:
                    break
                temp = self.cli.recv(lennn)

            lenc = int.from_bytes(content_len, byteorder='big', signed=False)
            json_bytes = []
            temp = self.cli.recv(lenc)
            while True:
                json_bytes += temp
                if not len(json_bytes) - lenc:
                    break
                temp = self.cli.recv(lenc)
            self.media_type = HEADER_JSON
            return json.loads(str(bytearray(json_bytes), "utf-8"))
        # chamador deve tratar casos binarios
        elif head == HEADER_FILE:
            self.media_type = HEADER_FILE
            return None


