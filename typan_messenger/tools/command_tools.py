import sys
from argparse import ArgumentParser
from typan_messenger.typan_client.client import Client
from typan_messenger.typan_server.tcp_server import TCPThreadingServer, JimHandler


def create_parser(prog, description,
                  port=7777, addr='127.0.0.1'):
    """
    Function for building commandline interface
    :param prog: the is must me Client or Server object
    :param description: nam
    :param port: port for using default 7777
    :param addr: addres for using default - 127.0.0.1
    :return:
    """
    parser = ArgumentParser(
        prog=prog,
        description=description
    )
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        default=port,
    )
    parser.add_argument(
        '-a',
        '--addr',
        default=addr,
        help=''
    )
    return parser


class Runner:
    def __init__(
            self,
            prog_client='client',
            prog_server='tcp_server',
            name_prog='TYPAN',
            port=7777,
            addr='127.0.0.1'
    ):
        self.addr = addr
        self.port = port
        self.server_parser = create_parser(
            prog_server,
            '{} server'.format(name_prog),
            addr=addr,
            port=port
        )
        self.client_parser = create_parser(
            prog_client,
            '{} client'.format(name_prog),
            addr=addr,
            port=port)


def run_client():
    parser = create_parser('client', 'TYPAN client')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    client = Client(addr, port)
    while True:
        msg = input()
        client.send_msg(msg)


def run_server():
    parser = create_parser('new_server', 'TYPAN server')
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    port = namespace.port
    server = TCPThreadingServer((addr, port), JimHandler)
    try:
        print('Start server {}'.format(server.server_address))
        server.serve_forever()
    except Exception:
        print('Oops!')
