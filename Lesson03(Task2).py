def func_y(x):
    if x < 0:
        y = abs(x) / x #abs(x) - модуль числа х
    elif x == 0:
        y = 0
    elif x > 0:
        y = x * x
    return (y)

print (func_y(7))