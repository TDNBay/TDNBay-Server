import logging
import socket
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
        self.s.listen(5)
        print("Servidor em execução.")
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



