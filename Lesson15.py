import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            msg = self.request.recv(1024)
            print(str(msg, 'utf-8'))
            print(msg.decode('utf-8'))

            response = b'''
            HTTP/1.1 200 OK/r
            Content-Type: text/html/r
            /r
        
            <h1>Hello<h1>'''

            self.request.sendall(response)


with socketserver.TCPServer(('', 8080), Handler) as server:     #'' = 127.0.0.1 - server IP (localhost) 8080 - server port
    server.serve_forever()