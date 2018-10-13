from request_parser.filehandler import FileRequestHandler
from request_parser.filelisthandler import FileListHandler
from request_parser.fileuploadhandler import FileUploadHandler

FILE_GET = 'fileget'
FILE_LIST = 'filelist'
FILE_UPLOAD = 'fileupload'

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
            if self.parsed_data['action'] == FILE_UPLOAD:
                return FileUploadHandler(self.client, self.parsed_data)