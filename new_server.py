from socketserver import BaseRequestHandler, TCPServer
import socket
import datetime
import sys
from http import HTTPStatus
import logging 

from jim.seriliazer import BaseJim
from tools.command_tools import create_parser

class TypanHandler(BaseRequestHandler):
    def handle(self):
        response = 'Hello world'
        print('Have request')
        if isinstance(self.request, socket.socket):
            print('Have request')

            response = BaseJim(status=200)
            self.request.sendall(bytes(response))

class TypanServer(TCPServer):
    pass


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