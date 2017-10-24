import sys
from argparse import ArgumentParser

def create_parser(prog, description, 
        port='help in progress', addr='help in progress'):

    parser = ArgumentParser(
        prog=prog,
        description=description
        )
    parser.add_argument(
        '-p', 
        '--port', 
        type=int, 
        default=7777, 
        help=port
        )
    parser.add_argument(
        '-a',
        '--addr', 
        default='127.0.0.1', 
        help=addr
        )
    return parser