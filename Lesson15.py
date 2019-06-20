import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            connection = self.request
            msg = connection.recv(1024)
            #print(str(msg, 'utf-8'))
            print(msg.decode('utf-8'))

            response_body = '<h1>Hello</h1>'

            response = f'''
HTTP/1.1 200 OK
Content-Type: text/html
Content-Lenght: {len(response_body)}
Connection: keep-alive

{(response_body)}'''

            connection.sendall(response.encode())


with socketserver.TCPServer(('', 8080), Handler) as server:     #'' = 127.0.0.1 - server IP (localhost) 8080 - server port
    server.serve_forever()