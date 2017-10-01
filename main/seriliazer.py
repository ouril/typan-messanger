import json
from http import HTTPStatus
from datetime import datetime

def server_message(code, alert=HTTPStatus.BAD_REQUEST.phrase):
    rendered= {
                'response': code,
                'time': str(datetime.now().time()),
                'alert': alert
            }
    return rendered

def message_validation(msg):
    try:
        unserilization_data = json.loads(msg.decode("utf-8"))
    except Exception as err:
        return False
        print("DATA ERROR: {}".format(err))
    if all(i for i in unserilization_data.values()):
        return unserilization_data

def render_message(
    action='present', 
    status='online',
    name='Test',
    msg='Hello, Server!'
    ):
    rendered = {
        'action': action,
        'time': str(datetime.now().time()),
        'type': status,
        'user': {
            'account_name': name,
            'status': msg
            }phrase
    }
    return rendered
