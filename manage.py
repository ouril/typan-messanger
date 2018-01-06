from argparse import ArgumentParser

from typan_messenger.typan_server.models import create_table
from typan_messenger.tools.command_tools import run_server, run_client


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
        if args.command == 'runserver':
            # TODO Added args for adding port and addr
            run_server()
        elif args.command == 'serverinit':
            create_table()
        elif args.command == 'clientinit':
            pass
        else:
            pass
    else:
        run_client()