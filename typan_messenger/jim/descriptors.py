class HTTPCode(object):
    code = CODES
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


    