import socket
import socketserver as sv

from typan_messenger.jim.seriliazer import server_jim, Jim
from typan_messenger.tools.log import server_logger
from typan_messenger.tools.decorators import Log


class JimHandler(sv.BaseRequestHandler):
    @Log(server_logger)
    def handle(self):
        while True:
            if isinstance(self.request, socket.socket):
                try:

                    req = self.request.recv(1024)
                    jim = Jim.from_bytes(req)
                    print(jim)
                except Exception as err:
                    pass
                else:
                    print(jim.to_dict())
                    print('Have request from')
                    response = server_jim()
                finally:
                    self.request.sendall(bytes(response))


class TCPThreadingServer(sv.ThreadingMixIn, sv.TCPServer):
    allow_reuse_address = True
