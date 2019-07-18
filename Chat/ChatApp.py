import socket, threading, re, json, time, sys, os
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

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
    NAME = "S"

    _pattern_end = re.compile(r'<end>$')

    def name_check(self):
        init_message = ""
        self.send(init_message)
        status = self.receive()
        return status


    def json_send(self, message, user=None):
        message_data = {
            "name": self.NAME,
            "message": message
        }
        if user:
            message_data.setdefault("to", user)
        json_data = json.dumps(message_data)
        data = '<client to server>: ' + str(json_data) +'<end>'
        return data

    def json_receive(self, response):
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

    def sender(self):
        connection_status = True
        while connection_status:
            message = input()
            if message == '.exit':
                connection_status = False
            else:
                connection_status = self.send(message)

    def send(self, message):
        pattern = re.compile(r'\.\w+')
        user = pattern.match(message)
        if user:
            user = user.group()
            user = user[1:]
            message = message[len(user)+2:]
            data = self.json_send(message, user=user)
        else:
            data = self.json_send(message)
        try:
            self.sock.sendall(bytes(data, 'ascii'))
            return True
        except ConnectionError:
            return False

    def receiver(self,):
        connection_status = True
        while connection_status:
            connection_status = self.receive()

    def receive(self):
        try:
            end_find = False
            response = ''
            while not end_find:
                received_data = str(self.sock.recv(1024), 'ascii')
                response = response + received_data
                if re.search(self._pattern_end, response):
                    end_find = True
        except ConnectionError:
            message = 'Connection lost. Press Enter to exit.'
            print(message)
            self.print(message)
            return False
        else:
            message = self.json_receive(response)
            if message == 'from server: Invalid name or name already used. Select another one.':
                print(message)
                self.print(message)
                return False
            print(message)
            self.print(message)
            return True

    def print(self, message):
        self.print_text(message)

    def chat_connect(self, _):
        self.IP = self.ip_textinput.text
        self.PORT = int(self.port_textinput.text)
        self.NAME = self.name_textinput.text

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            try:
                self.sock.connect((self.IP, self.PORT))

                s_thread = threading.Thread(target=self.sender, args=())
                r_thread = threading.Thread(target=self.receiver, args=())

                name_status = self.name_check()
                if name_status:
                    s_thread.start()
                    r_thread.start()

                    s_thread.join()
            except ConnectionRefusedError:
                message = "Can't connect to this server."
                print(message)
                self.print(message)




    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '720')
    Config.set('graphics', 'resizable', '0')

    def print_text(self, message):
        self.chat_lable.text = self.chat_lable.text + ('\n') + time.strftime('%H:%M:%S: ') + message

    def on_enter(self, instance):
        self.message = instance.text
        if self.message:
            instance.text = ''
            self.chat_lable.text = self.chat_lable.text + ('\n') + time.strftime('%H:%M:%S: ') + self.message

    def btn_press(self, instance):
        if instance.text == 'Connect':
            instance.text = 'Disconnect'
            instance.background_color = [0.5,0,0,1]
            Clock.schedule_once(self.chat_connect, 2)
        elif instance.text == 'Disconnect':
            instance.text = 'Connect'
            instance.background_color = [0,0.5,0,1]


    def build(self):

        fl = FloatLayout()

        self.connect_button = Button(text = 'Connect',
                                font_size=30,
                                on_press=self.btn_press,
                                background_color=[0,0.5,0,1],
                                background_normal='',
                                size_hint=[None, None],
                                size=(180, 50),
                                pos=(1050, 650))

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
                           pos=(10, 120))

        self.message_textinput = TextInput(font_size=30,
                                multiline=False,
                                size_hint=[None, None],
                                size=(1260, 100),
                                pos=(10, 10))

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


if __name__ == "__main__":
    ClientApp().run()
