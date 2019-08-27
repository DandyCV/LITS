import socket, threading, re, json, time
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

'''To start char enter connection parameters:
server ip: IP
server port: PORT
your nick name: NAME
Char commands:
.[user_name] [message] - private message to user [user_name]
.exit - exit from chat room'''


class ClientApp(App):

    IP = 'localhost'
    PORT = 8080
    NAME = "Lits"
    connection_status = False

    _pattern_end = re.compile(r'<end>$')
    # Make message <client to server>:{"name": user_name, "message": text_message, "to": recipient_name}<end>

    def name_check(self):
        # Return name validation status
        init_message = ""
        self.send(init_message)
        status = self.receive()
        return status

    def send(self, message):
        # Send message to server
        pattern = re.compile(r'\.\w+')  # Search for special commands (.User_name -> private message)
        user = pattern.match(message)
        if user:
            user = user.group()
            user = user[1:]
            message = message[len(user)+2:] # Cut off User_name from message
            data = self.json_send(message, user=user)   # Message convert to json
            self.chat_lable.text = self.chat_lable.text + '\n' + time.strftime('%H:%M:%S: ') + 'to '+user+': ' + message
            # Message time in chat window
        else:
            data = self.json_send(message)  # If no User_name -> all is message
        try:
            self.sock.sendall(bytes(data, 'ascii')) # Trying to send message to server and catching connection errors
            return True
        except ConnectionError:
            return False    # Return status of send message

    def json_send(self, message, user=None):
        # Make message <client to server>:{"name": user_name, "message": text_message, "to": recipient_name}<end>
        message_data = {
            "name": self.NAME,
            "message": message
        }
        if user:    # If we have User_name add this key
            message_data.setdefault("to", user)
        json_data = json.dumps(message_data)
        data = '<client to server>: ' + str(json_data) +'<end>'
        return data

    def receiver(self,):
        # While loop to listen socket for new messages from server
        connection_status = True
        while connection_status:
            connection_status = self.receive()

    def receive(self):
        # Reading data with 1024 bytes blocks from socket until <end> is find
        try:
            end_find = False
            response = ''
            while not end_find:
                received_data = str(self.sock.recv(1024), 'ascii')
                response = response + received_data
                if re.search(self._pattern_end, response):
                    end_find = True
        except ConnectionError: # Catching connection errors
            message = 'Disconnected from server.'
            print(message)
            self.print(message) # Print connection problems message
            self.connection_status = False
            return False
        else:
            message = self.json_receive(response)
            if message == 'from server: Invalid name or name already used. Select another one.':
                # Print this message if User_name is not valid
                print(message)
                self.print(message)
                return False
            print(message)
            self.print(message)
            return True

    def json_receive(self, response):
        # Pull out <sender_name>, <message>, <recipient_name>
        pattern_end = self._pattern_end
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

    def print(self, message):   # Print text in Label
        self.print_text(message)

    def chat_connect(self):
        # Connection to chat-server when press the button "Connect"
        self.IP = self.ip_textinput.text
        self.PORT = int(self.port_textinput.text)
        self.NAME = self.name_textinput.text

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            # Start context manager
            try:
                self.sock.connect((self.IP, self.PORT))
            # And new thread for receiving messages
                r_thread = threading.Thread(target=self.receiver, args=())
            # Name validation
                name_status = self.name_check()
                if name_status:
                    r_thread.start()
                    r_thread.join()
            # Catch connecting errors
            except TimeoutError:
                message = "Can't connect to server (server timeout)."
                print(message)
                self.print(message)
            except ConnectionRefusedError:
                message = "Can't connect to server (connection refused)."
                print(message)
                self.print(message)
            except socket.gaierror:
                message = "Can't connect to server (wrong IP)."
                print(message)
                self.print(message)

    def disconnect(self):
        # Close the socket if exit program
        self.sock.close()




    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '720')
    Config.set('graphics', 'resizable', '0')

    def print_text(self, message):
        # Add time to message and print it in Label
        self.chat_lable.text = self.chat_lable.text + '\n' + time.strftime('%H:%M:%S: ') + message

    def on_enter(self, instance):
        # Send message from text_input
        self.message = instance.text
        if self.message:
            instance.text = ''  # Clear text_input after sending message
            if self.connection_status == True:  # Do not send message if no connection
                self.send(self.message)

    def btn_press(self, instance):
        # Connection button
        if instance.text == 'Connect':
            connect_thread = threading.Thread(target=self.chat_connect, args=())
            self.connection_status = connect_thread.start() # Sending thread start
            time.sleep(1.5)
            if threading.active_count() == 3:   # If connected to server -> change Button
                self.connection_status = True
                self.connect_button.text = 'Disconnect'
                self.connect_button.background_color = [0.5, 0, 0, 1]

        elif instance.text == 'Disconnect':
            self.disconnect()
            self.connection_status = False
            instance.text = 'Connect'
            instance.background_color = [0,0.5,0,1]

    def build(self):
        # Chat client window constructor
        fl = FloatLayout()

        self.connect_button = Button(text = 'Connect',
                                font_size=30,
                                background_color=[0,0.5,0,1],
                                background_normal='',
                                size_hint=[None, None],
                                size=(180, 50),
                                pos=(1050, 650))
        self.connect_button.bind(on_press=self.btn_press)

        self.ip_lable = Label(text='IP',
                         font_size=30,
                         size_hint=[None, None],
                         size=(100, 50),
                         pos=(0, 650))

        self.ip_textinput = TextInput(font_size=30, text='localhost',
                         multiline=False,
                         size_hint=[None, None],
                         size=(240, 50),
                         pos=(80, 650))

        self.port_lable = Label(text='PORT',
                         font_size=30,
                         size_hint=[None, None],
                         size=(200, 50),
                         pos=(280, 650))

        self.port_textinput = TextInput(font_size=30, text='8080',
                         multiline=False,
                         size_hint=[None, None],
                         size=(100, 50),
                         pos=(430, 650))

        self.name_lable = Label(text='NAME',
                           font_size=30,
                           size_hint=[None, None],
                           size=(200, 50),
                           pos=(500, 650))

        self.name_textinput = TextInput(font_size=30, text = 'Lits',
                                   multiline=False,
                                   size_hint=[None, None],
                                   size=(340, 50),
                                   pos=(660, 650))

        self.chat_lable = Label(font_size=30,
                           text_size = (1260, 520),
                           size_hint=[None, None],
                           size=(1260, 520),
                           pos=(10, 120),
                           color=[0,0,0,1])
        with fl.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(10, 120), size=(1260,520))

        self.message_textinput = TextInput(font_size=30,
                                multiline=False,
                                size_hint=[None, None],
                                size=(1260, 100),
                                pos=(10, 10),
                                text_validate_unfocus = False)

        self.message_textinput.bind(on_text_validate=self.on_enter)


        fl.add_widget(self.ip_lable)
        fl.add_widget(self.ip_textinput)
        fl.add_widget(self.port_lable)
        fl.add_widget(self.port_textinput)
        fl.add_widget(self.name_lable)
        fl.add_widget(self.name_textinput)
        fl.add_widget(self.connect_button)


        fl.add_widget(self.chat_lable)
        fl.add_widget(self.message_textinput)
        return fl

    def on_stop(self):  # If application terminated -> close socket
        self.disconnect()


if __name__ == "__main__":
    client = ClientApp()
    client.run()