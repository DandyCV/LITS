import argparse

parser = argparse.ArgumentParser()   #зчитує аргументи командного рядка
# parser.add_argument('name')          #python 3.py 3('name')
# parser.add_argument('-l', '--len', action='source_true')   #'--len' - повне ім'я  action='source'-значення в терміналі запишеться
#                                                             #'-l', action='source_true' - значення l запишеться True
parser.add_argument('-l', '--len', dafault='len')            #-len запишеться 'len' по дефоту
#
# parser.add_argument('-l', '--len', dest='')                  #dest - дефолтне значення для зовн. виклику

# parser.add_argument('-l', '--len', choise=('345', 345))

print(parser.parser_args().len)

# python weather.py -lang(language - ua), -name(city - Чернівці)
select - бібліотека для сокетів