import datetime as dt
import http

CODE = [i.value for i in http.HTTPStatus]

class HTTPCode(object):
    code = CODE
    def __init__(self):
        self._status_code = 500
    
    def __get__(self, instanse, instanse_type):
        return self._status_code

    def __set__(self, instanse, value):
        if value in self.code:
            self._status_code = value
        else: 
            raise ValueError('Bad type data! You need instanse of HTTPStatus')

class MessageText(object):
    def __init__(self):
        self._msg = ''
    
    def __get__(self, instanse, instanse_type):
        return self._msg

    def __set__(self, instanse, value):
        if isinstance(value, type('str')) and len(value) < 256:
            self._msg = value
        else: 
            raise ValueError('Bad type data!')



class TimeField:
    def __init__(self):
        self._time = ''

    def __get__(self, instanse, instanse_type):
        return self._time

    def __set__(self, instanse, value):
        if isinstance(value, dt.datetime):
            self._time = str(value)
        else:
            raise ValueError('Bad type data!')
    