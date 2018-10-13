import subprocess
import uuid

from db import utils


class FileUploadHandler:

    def __init__(self, client, parsed_data):
        self.client = client
        self.parsed_data = parsed_data

    def handle_request(self):
        file_title = self.parsed_data['detail']
        file_name = uuid.uuid4().hex
        print(file_name)
        with open('files/' + file_name, 'wb') as f:
            while True:
                data = self.client.recv(16384)
                if not data:
                    break
                f.write(data)
            f.flush()
        self.get_thumb(file_name)
        utils.save_file(file_name, file_title)

    def get_thumb(self, file_name):
        result = subprocess.check_output(["lib/ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", "files/" + file_name])
        subprocess.run(["lib/ffmpeg", "-ss", str(float(result) / 2), "-i", "files/" + file_name, "-q:v", "2", "-vframes", "1", "files/thumb/" + file_name + ".png"])