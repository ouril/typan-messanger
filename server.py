import json
import sys
import select
from http import HTTPStatus
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
# from jim.seriliazer import server_message, message_validation
from tools.command_tools import create_parser
from tools.decorators import Log
from tools.log import server_logger

MAX_DATA_RECEIVE = 1024
MAX_CLIENT_CONNECTION = 10


class Server:
    '''
    >>> server = Server('127.0.0.1', 7777)
    TYPAN SERVER IS RUNNING...
    '''

    def __init__(self, addr, port):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.bind((addr, port))
            self.sock.listen(MAX_CLIENT_CONNECTION)
            print('TYPAN SERVER IS RUNNING...')
        except OSError as start_server_error:
            print('ERROR STARTING SERVER: {}'.format(start_server_error))
            sys.exit(1)

    @Log(server_logger)
    def send_response(self, code, client, addr):
        repr_response = server_message(code, HTTPStatus.OK.phrase)
        response = json.dumps(repr_response)
        try:
            client.send(response.encode('utf-8'))
            print('RESPONSE {} for {}'.format(HTTPStatus.OK.value, addr[0]))
        except OSError as err:
            print('ERROR RESPONSE {0}: {1}'.format(err))

    @Log(server_logger)
    def parse_data_from_cliet(self, client, addr, data):
        msg = message_validation(data)
        if msg:
            print('REQUEST FROM {}'.format(addr[0]))
            code = HTTPStatus.OK.value
        else:
            code = HTTPStatus.BAD_REQUEST.value
        self.send_response(code, client, addr)


    @Log(server_logger)
    def start(self):
        clients = []
        while True:
            try:
                client, addr = self.sock.accept()
            except OSError as err:
                pass
            else:
                print('new connection with %s' % str(addr))
                clients.append(client)
            finally:
                w = []
                try:
                    r, w, e = select.select([], clients, [], 0)
                except Exception as err:
                    pass
                for s_client in w:
                    data = s_client.recv(MAX_DATA_RECEIVE)
                    self.parse_data_from_cliet(client, addr, data)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    parser = create_parser('server', 'TYPAN server')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    server = Server(addr, port)
    server.start()
