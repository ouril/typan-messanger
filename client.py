import json
import typan_messenger.sys
from argparse import ArgumentParser
from http import HTTPStatus
from typan_messenger.socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
from typan_messenger.jim.seriliazer import *
from typan_messenger.tools.command_tools import create_parser
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
            typan_messenger.sys.exit(1)

    @log
    def disconnect_server(self):
        try:
            self.sock.close()
            print('CONNECTION EXIT')
        except OSError as disconnect_server_error:
            print('RESPONSE ERROR: {}'.format(disconnect_server_error))

    @Log(client_logger)
    def send_msg(self, msg):
        _msg = JimMessage()
        _msg.message = msg
        _msg.action = ''
        print(bytes(_msg))
        self.sock.send(bytes(_msg))
        print('Client send presence')


if __name__ == '__main__':
    parser = create_parser('client', 'TYPAN client')
    namespace = parser.parse_args(typan_messenger.sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    client = Client(addr, port)
    while True:
        msg = input()
        client.send_msg(msg)
