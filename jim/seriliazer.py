import json
from http import HTTPStatus
from config import MAX_LEN_MESSAGE
#from config import *
#from .errors import MandatoryKeyError, ResponseCodeError, ResponseCodeLenError


class HTTPCode(object):
    def __init__(self):
        self._status_code = HTTPStatus.OK
    
    def __get__(self, instance, instance_type):
        return self._status_code.value

    def __set__(self, instance, value):
        if isinstance(HTTPStatus, value):
            self._status_code = value
        else: 
            raise ValueError('Bad type data! You need instanse of HTTPStatus')
    def __bytes__(self):
        return self._status_code.value

class MessageText(object):
    def __init__(self):
        self._msg = ''
    
    def __get__(self, instance, instance_type):
        return self._msg

    def __set__(self, instance, value):
        if type(value) == 'str' and len(value) < MAX_LEN_MESSAGE:
            self._status_code = value
        else: 
            raise ValueError('Bad type data! You need instanse of HTTPStatus')

    def __bytes__(self):
        return self._msg

    
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


class JimHTTPResponse(BaseJim):

    def __init__(self, code):
        self.status_code = code