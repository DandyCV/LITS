import threading
import socketserver
import re
import json


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    connections = dict()
    name = "server"
    pattern_end = re.compile(r'<end>$')
    pattern_name = re.compile(r'\w+')

    def connection_init(self, connection):
        self.connections.update({connection: '__NEW_USER__'})
        data, socket_status = self.message_processor(connection)
        try:
            message = self.from_json(data)
        except RuntimeError and IndexError:
            print('Message to server not valid from: {}'.format(connection))
            self.connections.pop(connection)
            return False
        else:
            name = message["name"]
            response, name_status = self.name_check(name)
            data, user = self.to_json(response)
            self.socket_processor(data, user=user)
            if name_status:
                self.connections[connection] = name
                print('New user connected name: {}'.format(name))
            else:
                self.connections.pop(connection)
            return name_status

    def name_check(self, user):
        valid_name = re.match(self.pattern_name, user)
        users = list(self.connections.values())
        if not valid_name or user in users:
            user_message = "Invalid name or name already used. Select another one."
            response = {"name": self.name, "message": user_message, "to": "__NEW_USER__"}
            name_status = False
        else:
            new_user = user + ' connected.'
            response = {"name": self.name, "message": new_user}
            name_status = True
        return response, name_status

    def socket_processor(self, data, user=None):
        response = bytes(data, "ascii")
        try:
            if user:
                for address in self.connections.keys():
                    if self.connections[address] == user:
                        address.sendall(response)
            else:
                for address in self.connections.keys():
                    address.sendall(response)
        except ConnectionError:
            return False
        return True

    def to_json(self, message):
        user = None
        try:
            user = message["to"]
        except KeyError:
            send_to = "<server to all clients>: "
        else:
            send_to = "<server to client>: "
        data = send_to + json.dumps(message) + "<end>"
        return data, user

    def from_json(self, message):
        pattern_end = self.pattern_end
        pattern_start = re.compile(r'^<client to server>: ')
        _data1 = re.split(pattern_start, message, maxsplit=1)
        _data2 = re.split(pattern_end, _data1[1], maxsplit=1)
        data_json = _data2[0]
        print("{}: {}".format(ip, data_json))
        data = json.loads(data_json)
        return data

    def message_processor(self, connection):
        try:
            end_find = False
            data = ''
            while not end_find:
                received_data = str(self.request.recv(1024), "ascii")
                data = data + received_data
                if re.search(self.pattern_end, data):
                    end_find = True
            socket_status = True
        except ConnectionError:
            name = self.connections.pop(connection)
            user_msg = "{} disconnected".format(name)
            json_msg = '{"name": "server", "message": "' + user_msg + '"}'
            data = '<client to server>: ' + json_msg + '<end>'
            socket_status = False
        return data, socket_status

    def message_server(self, connection):
        socket_status = True
        connection_status = True
        while socket_status and connection_status:
            data, socket_status = self.message_processor(connection)
            message = self.from_json(data)
            json_data, user = self.to_json(message)
            connection_status = self.socket_processor(json_data, user=user)

    def handle(self):
        connection = self.request
        name_status = self.connection_init(connection)
        if name_status:
            self.message_server(connection)



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 8080

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
            ip, port = server.server_address
            # Start a thread with the server -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=server.serve_forever)
            # Exit the server thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print("Server loop running")
            server_thread.join()

