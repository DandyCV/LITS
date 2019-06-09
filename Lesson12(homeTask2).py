import os
class AOpen:

    def __init__(self, file_name, mode = 'rw', encoding = 'utf-8'):
        self.file_name = file_name
        self.encoding = encoding
        if mode == 'r': self.mode = os.O_RDONLY
        elif mode == 'w': self.mode = os.O_WRONLY
        elif mode == 'rw': self.mode = os.O_RDWR
        elif mode == 'a': self.mode = os.O_WRONLY | os.O_APPEND
        elif mode == 'ra': self.mode = os.O_RDWR | os.O_APPEND
        elif mode == 'wa': self.mode = os.O_WRONLY | os.O_APPEND
        self.fd = (os.open(self.file_name, self.mode))
        self.file = os.fdopen(self.fd)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, bytes = None):
        stat_info = os.stat(self.file_name)
        if bytes is None:
            bytes = stat_info.st_size
        byte_file = os.read(self.fd, bytes)
        return byte_file.decode(self.encoding)

    def readline(self):
        start = 1
        str_list = []
        while start:
            byte = os.read(self.fd, 1)
            str = byte.decode(self.encoding)
            if str == '\n':
                start = 0
            else:
                str_list.append(str)
        return ''.join(str_list)

    def readlines(self):
        lines_list = []
        while ''.join(str_list):
            start = 1
            str_list = []
            while start:
                byte = os.read(self.fd, 1)
                str = byte.decode(self.encoding)
                if str == '\n':
                    start = 0
                else:
                    str_list.append(str)
            lines_list.append(''.join(str_list))

    def write(self, text):
        text = text.encode(self.encoding)
        return os.write(self.fd, text)

    def seek(self, value):
        os.lseek(self.fd, value, os.SEEK_SET)

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)

    def writeline(self, text):
        text_line = ('\n' + text).encode(self.encoding)
        return os.write(self.fd, text_line)

    def writelines(self, text_list):
        for text in text_list:
            text_line = ('\n' + text).encode(self.encoding)
            os.write(self.fd, text_line)

    def close(self):
        self.fd.close()



file = AOpen('text.txt', 'ra', encoding = 'utf-8')
#file.write('Hello!')
#print(file.read())
#file.seek(0)
#print(file.tell())
file.writelines(['Good Morning!', 'Good Night'])
#print(file.readline())
#with AOpen('text.txt', 'ra', encoding = 'utf-8') as file:
    #print(file.read())
    #file.writelines(['Good Morning!', 'Good Night'])
    #print(file.readlines())
