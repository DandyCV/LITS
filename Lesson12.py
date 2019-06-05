import sys
import io
hendler = open('text.json', mode='rb')

print(dir(hendler), hendler.read(), sep='\n')
for line in hendler.readline():
    print(line)
# print(sys.stdin, sys.stdout, sys.stderr, sep='\n')
#
# n = 1
# try:
#     print(2 / n)
#     assert 2 > n
# except (ArithmeticError, AssertionError) as err:
#     print(f'error type {err}')
# else:
#     print('done!')
# finally:
#     print('finally print')

# for err in Exception.__subclasses__():
#     print(err)