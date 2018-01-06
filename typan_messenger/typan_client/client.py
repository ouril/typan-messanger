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
    @log
    def __init__(self, addr, port):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((addr, port))
            print('TYPAN CLINT ARE READY...')
        except OSError as start_server_error:
            print('ERROR STARTING TYPAN CLINT: {}'.format(start_server_error))
            sys.exit(1)

    @log
    def disconnect_server(self):
        try:
            self.sock.close()
            print('CONNECTION EXIT')
        except OSError as disconnect_server_error:
            print('RESPONSE ERROR: {}'.format(disconnect_server_error))

    @Log(client_logger)
    def send_msg(self, msg):
        _msg = PARAMS_FOR_JIM
        _msg['message'] = msg
        _msg['action'] = 'presence'
        _msg['time'] = str(dt.datetime.now())
        print(bytes(Jim(**_msg)))
        self.sock.send(bytes(Jim(**_msg)))
        print('Client send presence')


