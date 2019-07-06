import socket
import threading
import re
import json

'''To start char enter connection parameters:
server ip: IP
server port: PORT
your nick name: NAME

Char commands:
.[user_name] [message] - private message to user [user_name]
.exit - exit from chat room'''

IP = 'localhost'
PORT = 8080
NAME = ""

_pattern_end = re.compile(r'<end>$')

def name_check():
    init_message = ""
    send(init_message)
    status = receive()
    return status


def json_send(message, user=None):
    message_data = {
        "name": NAME,
        "message": message
    }
    if user:
        message_data.setdefault("to", user)
    json_data = json.dumps(message_data)
    data = '<client to server>: ' + str(json_data) +'<end>'
    return data


def json_receive(response):
        pattern_end = _pattern_end
        pattern_start = re.compile(r'^<server to \w+.\w+>: ')
        _data1 = re.split(pattern_start, response, maxsplit=1)
        _data2 = re.split(pattern_end, _data1[1], maxsplit=1)
        json_data = _data2[0]
        data = json.loads(json_data)
        message = data['message']
        name = data['name']
        try:
            user = data['to']
        except KeyError:
            text = name + ': ' + message
        else:
            text = 'from ' + name + ': ' + message
        return text


def sender():
    connection_status = True
    while connection_status:
        message = input()
        if message == '.exit':
            connection_status = False
        else:
            connection_status = send(message)


def send(message):
    pattern = re.compile(r'\.\w+')
    user = pattern.match(message)
    if user:
        user = user.group()
        user = user[1:]
        message = message[len(user)+2:]
        data = json_send(message, user=user)
    else:
        data = json_send(message)
    try:
        sock.sendall(bytes(data, 'ascii'))
        return True
    except ConnectionError:
        return False


def receiver():
    connection_status = True
    while connection_status:
        connection_status = receive()


def receive():
    try:
        end_find = False
        response = ''
        while not end_find:
            received_data = str(sock.recv(1024), 'ascii')
            response = response + received_data
            if re.search(_pattern_end, response):
                end_find = True
    except ConnectionError:
        print('Connection lost. Press Enter to exit.')
        return False
    else:
        message = json_receive(response)
        if message == 'from server: Invalid name or name already used. Select another one.':
            print(message)
            return False
        print(message)
        return True


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect((IP, PORT))

        s_thread = threading.Thread(target=sender, args=())
        r_thread = threading.Thread(target=receiver, args=())

        name_status = name_check()
        if name_status:
            s_thread.start()
            r_thread.start()

            s_thread.join()
    except ConnectionRefusedError:
        print ("Can't connect to this server.")

