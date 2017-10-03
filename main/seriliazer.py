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
        print("DATA ERROR: {}".format(err))
    if 'user' in unserilization_data.keys():
        user_data = unserilization_data['user']
        if not all(i for i in user_data.values()):
            return None
    if all(i for i in unserilization_data.values()):
        return unserilization_data
    
def render_message(
    action='present', 
    type_msg='test',
    name='Test',
    status='online'
    ):
    rendered = {
        'action': action,
        'time': str(datetime.now().time()),
        'type': type_msg,
        'user': {
            'account_name': name,
            'status': status
            }
    }
    return rendered
