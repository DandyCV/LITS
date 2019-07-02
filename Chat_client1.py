import socket
import threading
import time
import re

ip = 'localhost'
port = 8080
name = 'Dan'


def json_func(message, user=None):
    json_data = {
        'name': name,
        'message': message
    }
    if user:
         json_data.setdefault('to', user)
    data = '<client to server>: ' + str(json_data) +'<end>'
    return data


def send():
    while True:
        message = input()
        if message == '.exit':
            break
        elif message:
            pattern = re.compile(r'\.\w+')
            user = pattern.match(message)
            if user:
                user = user.group()
                user = user[1:]
                message = message[len(user)+2:]
                data = json_func(message, user=user)
            else:
                data = json_func(message)
            sock.sendall(bytes(data, 'ascii'))
            time.sleep(1)


def receive():
    while True:
        try:
            response = str(sock.recv(1024), 'ascii')
        except ConnectionAbortedError:
            break
        print("Received: {}".format(response))
        time.sleep(1)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))

    s_thread = threading.Thread(target=send, args=())
    r_thread = threading.Thread(target=receive, args=())

    s_thread.start()
    r_thread.start()

    s_thread.join()