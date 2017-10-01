import json 
import sys
from argparse import ArgumentParser
from http import HTTPStatus
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
from seriliazer import render_message, message_validation
from command_tools import create_parser

MAX_DATA_RECEIVE = 1024


class Client:

    def __init__(self, addr, port):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((addr, port))
            print('TYPAN CLINT ARE READY...')
        except OSError as start_server_error:
            print('ERROR STARTING TYPAN CLINT: {}'.format(start_server_error))
            sys.exit(1)

    def disconnect_server(self):
        try:
            self.sock.close()
            print('CONNECTION EXIT')
        except OSError as disconnect_server_error:
            print('RESPONSE ERROR: {}'.format(disconnect_server_error))

        
    def send_presence_msg(self):
        msg = json.dumps(render_message()).encode("utf-8")
        try:
            self.sock.send(msg)

            print('Client send presence')
        except OSError as socket_send_msg_error:
            print('RESPONSE ERROR: {}'.format(
                socket_send_msg_error)
            )
        data = self.sock.recv(MAX_DATA_RECEIVE)
        unserialized_data = message_validation(data)
        if unserialized_data and unserialized_data.get('response') == 200:
            print('{}! IT\'S WORKED!'.format(
                unserialized_data.get('alert')
            ))
        elif unserialized_data.get('response') == 400:
            print('REQUEST ERROR: {}'.format(
                unserialized_data.get('error')
            )) 
        else:
            print('UNKNOWN ERROR')
        self.disconnect_server()

if __name__ == '__main__':
    parser = create_parser('client', 'TYPAN client')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    client = Client(addr, port)
    client.send_presence_msg()
    
