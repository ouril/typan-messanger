import socket
import datetime
import sys
import logging
import json
from http import HTTPStatus
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

from jim.seriliazer import ServerResponse, JimMessage
from tools.command_tools import create_parser
from tools.log import server_logger
from tools.decorators import Log


class TypanHandler(BaseRequestHandler):
    @Log()
    def handle(self):
        if isinstance(self.request, socket.socket):
            req = self.request.recv(1024)
            jim = JimMessage.from_bytes(req)

            print(jim.__dict__)
            print('Have request 2')
            response = ServerResponse()

            self.request.sendall(bytes(response))


class TypanServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True


if __name__ == '__main__':
    parser = create_parser('new_server', 'TYPAN server')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    server = TypanServer((addr, port), TypanHandler)
    try:
        print('Start server {}'.format(server.server_address))
        server.serve_forever()
    except Exception:
        print('Oops!')
