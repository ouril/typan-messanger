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
    def __init__(self, addr, port):
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
            self.sock.send(bytes(Jim(**_msg)))
        except Exception as err:
            print(err)
        return _msg

    def login(self):
        self.user = input("Input username >>>")
        return self.user

    def get_contact_list(self):
        msg = self.send_msg(
            action="contact_list",
            from_user=self.user,
            to='server',
        )
        return msg

    def add_contact(self, contact):
        pass

    def del_contact(self, contact):
        pass