import socket
import threading
import time


ip = 'localhost'
port = 8080


def send():
    while True:
        message = input()
        if message == '.exit':
            break
        if message:
            sock.sendall(bytes(message, 'ascii'))
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