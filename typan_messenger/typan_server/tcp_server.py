import socket
import socketserver as sv
import datetime as dt

from typan_messenger.jim.seriliazer import server_jim, Jim
from typan_messenger.tools.log import server_logger
from typan_messenger.tools.decorators import Log
from config import PARAMS_FOR_JIM
from .contacts import ServerContactList


class JimHandler(sv.BaseRequestHandler):

    def send_msg(self, msg='', action='presense', to='',
                 from_user='', encoding='', room=''):
        _msg = PARAMS_FOR_JIM
        _msg['message'] = msg
        _msg['action'] = action
        _msg['from_user'] = from_user
        _msg['to'] = to
        _msg['time'] = str(dt.datetime.now())
        _msg['room'] = room
        _msg['encoding'] = encoding
        _msg['room'] = room
        try:
            self.request.send(bytes(Jim(**_msg)))
        except Exception as err:
            print(err)
        return _msg

    @Log(server_logger)
    def handle(self):
        while True:
            if isinstance(self.request, socket.socket):
                try:
                    req = self.request.recv(1024)
                    jim = Jim.from_bytes(req)
                except Exception as err:
                    pass
                else:
                    if jim.action == "get_contacts":
                        contact_list = ServerContactList.build_from_base(jim.user)
                        response = server_jim(code=202, msg=len(contact_list))
                        self.request.send(bytes(response))
                        try:
                            for contact in contact_list:
                                msg = "{}  {}".format(contact[0], contact[1])
                                self.send_msg(msg=msg, action="contact_list")
                        except Exception as err:
                            print(err)
                            response = server_jim(code=500, msg=err)
                            self.request.send(bytes(response))
                finally:
                    pass


class TCPThreadingServer(sv.ThreadingMixIn, sv.TCPServer):
    allow_reuse_address = True
