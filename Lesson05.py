def check_float(s):
    if '.' in s:
        return True
    else:
        return False
s = '5.8'
print (check_float(s))

def decor(func):
    def inner(*args, **kw):
        print ('\n')
        func()
        print('\n')
    return inner

@decor
def smart_input():
    numbers = input('Введіть кілька чисел через пробіл ')
    numbers_list = numbers.split()
    max = float('-inf')
    for n in numbers_list:
        num = int(n)
        if num > max:
                max = num
    print('Максимальне число = ',max)
                                            #def max_input():
                                            #print(max(map(int,input().split())))
smart_input()



