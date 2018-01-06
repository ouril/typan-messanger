import socket
import socketserver as sv

from typan_messenger.jim.seriliazer import ServerResponse, JimMessage
from typan_messenger.tools.log import server_logger
from typan_messenger.tools.decorators import Log

log = Log(server_logger)


class JimHandler(sv.BaseRequestHandler):
    @log
    def handle(self):
        while True:
            if isinstance(self.request, socket.socket):
                try:
                    req = self.request.recv(1024)
                    jim = JimMessage.from_bytes(req)
                except Exception as err:
                    pass
                else:
                    print(jim.__dict__)
                    print('Have request from')
                    response = ServerResponse()
                finally:
                    self.request.sendall(bytes(response))


class TCPThreadingServer(sv.ThreadingMixIn, sv.TCPServer):
    allow_reuse_address = True



