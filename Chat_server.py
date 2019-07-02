import threading
import socketserver
import socket


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    connections = []
    users = []

    def socket_processor(self, data):
        response = bytes(data, "ascii")
        for address in self.connections:
            address.sendall(response)

    def message_processor(self):
        while True:
            try:
                data = str(self.request.recv(1024), "ascii")
            except ConnectionError:
                break
            print("{}: {}".format(ip, data))
            self.socket_processor(data)


    def handle(self):
        conn = self.request
        self.connections.append(conn)
        print('New user connected')
        response = bytes('You has connected to server.', "ascii")
        self.request.sendall(response)
        self.message_processor()
        self.connections.remove(conn)
        data = 'User disconnected'
        self.socket_processor(data)


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
            # print("Server loop running in thread:", server_thread.name)
            server_thread.join()

