#!/usr/bin/env python

from argparse import ArgumentParser

from typan_messenger.typan_server.models import ServerDB
from typan_messenger.tools.command_tools import run_server, run_client
from typan_messenger.typan_client.gui_client import run_client_gui
from typan_messenger.typan_client.models import create_client_db

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-c',
        '--command'
    )
    parser.add_argument(
        '-p',
        '--port'
    )
    parser.add_argument(
        '-a',
        '--addr'
    )
    args = parser.parse_args()
    if args.command:
        print(args.command)
        if args.command == 'runserver':
            run_server()
        elif args.command == 'serverinit':
            server = ServerDB()
            server.create_table()
        elif args.command == 'clientinit':
            create_client_db()
        else:
            pass
    else:
        run_client_gui()
