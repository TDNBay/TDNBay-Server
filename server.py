import logging
import socket
import subprocess
import traceback
from threading import Thread

from request_parser.reqparser import ParsedRequest
from request_parser.router import RequestRouter


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((host, port))

    def listen(self):
        Thread(target=self.runImageServer).start()
        self.s.listen(5)
        print("Servidor em execução na porta", self.port)
        while True:
            try:
                cli, addr = self.s.accept()
                print("Nova conexão, origem:", addr)
                cli.settimeout(60)
                Thread(target=self.handleClient, args=(cli, addr)).start()
            except Exception as e:
                logging.error(traceback.format_exc())



    def handleClient(self, client, addr):
        pr = ParsedRequest(client)
        parsed = pr.parse()
        router = RequestRouter(parsed, client)
        handler = router.route()
        handler.handle_request()
        client.close()

    def runImageServer(self):
        subprocess.run(["python", "-m", "http.server"])



