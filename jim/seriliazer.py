import json
from http import HTTPStatus
import datetime

# from config import *
# from .errors import MandatoryKeyError, ResponseCodeError, ResponseCodeLenError
CODES = (200, 400, 500)
# actions: authenticate, presence, quit, msg, join, leave, probe (server)
# fields: action, time, user (account_name, status), type, to, from, encoding, message, room

BASE_MSG_DICT = dict(
    action='presence',
    time=str(datetime.datetime.now()),
    user='Test',
    type='Test'
)


class BaseJim:

    def __init__(self, **kwargs):
        """
        :param kwargs: любые именованные параметры для формирования сообщения
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __bytes__(self):
        """Возможность приводить сообщение сразу в байты bytes(jim_message)"""
        message_json = json.dumps(self.__dict__)
        message_bytes = message_json.encode(encoding='utf-8')
        return message_bytes

    @classmethod
    def from_bytes(cls, message_bytes):
        """Возможность создавать сообщение по набору байт"""
        message_json = message_bytes.decode(encoding='utf-8')
        message_dict = json.loads(message_json)
        return cls(**message_dict)

    def __str__(self):
        return str(self.__dict__)


class JimMessage(BaseJim):
    def __init__(self, *args, **kwargs):
        super(JimMessage, self).__init__(**kwargs)


class ServerResponse(BaseJim):
    def __init__(self, *args, **kwargs):
        self.errors = 'OK'
        self.status_code = 200
        super(ServerResponse, self).__init__(**kwargs)


if __name__ == '__main__':
    a = JimMessage()
    a.message = 888
    b = ServerResponse()
    b.status_code = 200
    print(bytes(b))
    print(bytes(a))
