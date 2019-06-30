import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


# import socket
# import threading
# import socketserver
#
# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         data = str(self.request.recv(1024), 'ascii')
#         cur_thread = threading.current_thread()
#         print("{} wrote:".format(self.client_address[0]))
#         print(data)
#         response1 = bytes("{} wrote:".format(self.client_address[0]), 'ascii')
#         response2 = bytes(data, 'ascii')
#         self.request.sendall(response1)
#         self.request.sendall(response2)
#
#
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass
#
#
# def client(ip, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((ip, port))
#         sock.sendall(bytes(message, 'ascii'))
#         response = str(sock.recv(1024), 'ascii')
#         print("Received: {}".format(response))
#
#
# if __name__ == "__main__":
#     # Port 0 means to select an arbitrary unused port
#     HOST, PORT = "localhost", 8080
#
#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     with server:
#         ip, port = server.server_address
#
#         # Start a thread with the server -- that thread will then start one
#         # more thread for each request
#         server_thread = threading.Thread(target=server.serve_forever)
#         print("Server loop running in thread:", server_thread.name)
#         # Exit the server thread when the main thread terminates
#         server_thread.daemon = True
#         server_thread.start()
#         client(ip, port, "Hello World 1")
#         print(ip, port)
#         client(ip, port, "Hello World 2")
#         print(ip, port)
#         client(ip, port, "Hello World 3")
#         print(ip, port)
#         server.serve_forever()

        # server.shutdown()
