from request_parser.filehandler import FileRequestHandler

FILE_GET = 'fileget'
FILE_LIST = 'filelist'

class RequestRouter:

    def __init__(self, parsed_data, client):
        self.parsed_data = parsed_data
        self.client = client

    def route(self):
        if self.parsed_data:
            if self.parsed_data['action'] == FILE_GET:
                return FileRequestHandler(self.client, self.parsed_data)
            if self.parsed_data['action'] == FILE_LIST:
                return FileListHandler(self.client, self.parsed_data)