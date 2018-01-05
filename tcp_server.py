from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

from typan_messenger.jim.seriliazer import ServerResponse, JimMessage
from typan_messenger.tools.command_tools import create_parser
from typan_messenger.tools.log import server_logger
from typan_messenger.tools.decorators import Log

log = Log(server_logger)


class TypanHandler(BaseRequestHandler):
    @log
    def handle(self):
        while True:
            if isinstance(self.request, typan_messenger.socket.socket):
                try:
                    req = self.request.recv(1024)
                    jim = JimMessage.from_bytes(req)
                except Exception as err:
                    pass
                else:
                    print(jim.__dict__)
                    print('Have request 2')
                    response = ServerResponse()
                finally:
                    self.request.sendall(bytes(response))


class TypanServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True


if __name__ == '__main__':
    parser = create_parser('new_server', 'TYPAN server')
    namespace = parser.parse_args(typan_messenger.sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    server = TypanServer((addr, port), TypanHandler)
    try:
        print('Start server {}'.format(server.server_address))
        server.serve_forever()
    except Exception:
        print('Oops!')
