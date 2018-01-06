import json
import collections as col
import datetime as dt
from config import BASE_LIST, PARAMS_FOR_JIM
Base = col.namedtuple('Jim', BASE_LIST)


class Jim(Base):

    def to_dict(self):
        return dict(self._asdict())

    def __bytes__(self):
        message_json = json.dumps(self.to_dict())
        message_bytes = message_json.encode(encoding='utf-8')
        return message_bytes

    @classmethod
    def from_bytes(cls, message_bytes):
        message_json = message_bytes.decode(encoding='utf-8')
        message_dict = json.loads(message_json)
        return cls(**message_dict)

    def now(self):
        return self._replace(time=str(dt.datetime.now()))


def server_jim(code=500, msg='SERVER_ERROR'):
    params = PARAMS_FOR_JIM
    params['status'] = code
    params['message'] = msg
    params['user'] = 'server'
    params['action'] = 'answer'
    server_msg = Jim(**params)
    return server_msg.now()
