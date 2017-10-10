import logging
from datetime import datetime

from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(self, *argv, **kwargv):
        _format = logging.Formatter('%(levelname)-10s%(asctime)s%(message)s')
        info_log = logging.FileHendler('server.log')
        info_log.setFormatter(_format)
        info_log.setLevel(logging.INFO)
        server_log = logging.getLogger('server')
        res = func(*args, **kwargs)
        return func(self, *argv, **kwargv)
    return wrapper

class Log:

    def __init__(self, 
                app=str(datetime.today())+'server', 
                filer=str(datetime.today())+'server.log'):
        self.app = app
        self.file = filer

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            _format = logging.Formatter('%(levelname)-10s%(asctime)s%(message)s')
            info_log = logging.FileHendler('server.log')
            info_log.setFormatter(_format)
            info_log.setLevel(logging.INFO)
            server_log = logging.getLogger(self.app)
            res = func(*args, **kwargs)
            return res
        return decorated


        