import socket
import datetime
import sys
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

from jim.seriliazer import ServerResponse, JimMessage
from tools.command_tools import create_parser
from tools.log import server_logger
from tools.decorators import Log

log = Log(server_logger)


class TypanHandler(BaseRequestHandler):
    @log
    def handle(self):
        if isinstance(self.request, socket.socket):
            req = self.request.recv(1024)
            jim = JimMessage.from_bytes(req)

            print(jim.__dict__)
            print('Have request 2')
            response = ServerResponse()

            self.request.sendall(bytes(response))


if __name__ == '__main__':
    parser = create_parser('new_server', 'TYPAN server')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    server = TCPServer((addr, port), TypanHandler)
    try:
        print('Start server {}'.format(server.server_address))
        server.serve_forever()
    except Exception:
        print('Oops!')
