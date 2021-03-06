import sys
import datetime as dt
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
from typan_messenger.jim.seriliazer import *
from config import PARAMS_FOR_JIM
from typan_messenger.tools.decorators import Log
from typan_messenger.tools.log import client_logger

MAX_DATA_RECEIVE = 1024

log = Log(client_logger)


class Client:
    @Log(client_logger)
    def __init__(self, addr='127.0.0.1', port=7777):
        self.user = 'anonimus'
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((addr, port))
            print('TYPAN CLINT ARE READY...')
        except OSError as start_server_error:
            print('ERROR STARTING TYPAN CLINT: {}'.format(start_server_error))
            sys.exit(1)

    @Log(client_logger)
    def disconnect_server(self):
        try:
            self.sock.close()
            print('CONNECTION EXIT')
        except OSError as disconnect_server_error:
            print('RESPONSE ERROR: {}'.format(disconnect_server_error))

    @Log(client_logger)
    def send_msg(self, msg='', action='presense', to='anonym',
                 from_user='', encoding='', room=''):
        _msg = PARAMS_FOR_JIM
        _msg['message'] = msg
        _msg['action'] = action
        _msg['from_user'] = from_user
        _msg['to'] = to
        _msg['time'] = str(dt.datetime.now())
        _msg['encoding'] = encoding
        _msg['room'] = room
        try:
            self.sock.send(bytes(Jim(**_msg)))
        except Exception as err:
            print(err)
        return _msg

    # TODO: Must be exception
    def login(self, user="anonym"):
        if type(user) == 'str':
            self.user = user
            return self.user
        else:
            return None

    def get_contact_list(self):
        msg = self.send_msg(
            action="get_contacts",
            from_user=self.user
        )
        return msg

    def add_contact(self, contact):
        msg = self.send_msg(
            msg=contact,
            action="add_contact",
            from_user=self.user
        )
        return msg

    def del_contact(self, contact):
        msg = self.send_msg(
            action="del_contact",
            from_user=self.user,
            msg=contact
        )
        return msg
