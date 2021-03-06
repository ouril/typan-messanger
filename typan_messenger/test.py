import unittest
import json
from subprocess import Popen, PIPE
from seriliazer import server_message, message_validation, render_message


def test_server_message():
    msg = server_message(666, alert='AHAHAHA!!!')
    assert msg['response'] == 666
    assert msg['alert'] == 'AHAHAHA!!!'


def test_render_message():
    msg = render_message(action='unknown', type_msg='try')
    assert msg['type'] == 'try'
    assert msg['action'] == 'unknown'


def test_validation():
    msg = json.dumps(server_message(code=100))
    assert message_validation(msg.encode('utf-8'))['response'] == 100


class TestFunctions(unittest.TestCase):

    def test_client_server_connections(self):
        server = Popen(['python3', 'server.py'], stdout=None)
        answer = Popen(['python3', 'client.py'], stdout=PIPE)
        self.assertEqual(str(answer.stdout.read().decode('utf-8')),
                         'TYPAN CLINT ARE READY...\nClient send presence\nOK! IT\'S WORKED!\nCONNECTION EXIT\n')
        server.kill()

    def test_server_message(self):
        msg = server_message(101)
        self.assertEqual(msg['response'], 101)
        self.assertEqual(msg['alert'], 'Bad Request')

    def test_render_message(self):
        msg = render_message(name='unknown', type_msg='try')
        self.assertEqual(msg['type'], 'try')
        self.assertEqual(msg['user']['account_name'], 'unknown')
        self.assertEqual(msg['user']['status'], 'online')

    def test_validation(self):
        msg = json.dumps(render_message(name=''))
        msg_right = json.dumps(render_message(action='ok'))
        self.assertFalse(message_validation(msg.encode('utf-8')))
        self.assertEqual(message_validation(msg_right.encode('utf-8'))['action'], 'ok')


if __name__ == '__main__':
    unittest.main()
