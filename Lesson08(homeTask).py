def sort_1():
    list_1 = input('Через пробіл введіть числа для сортування: ')
    list_1 = list_1.split()
    list_int = []
    list_float = []
    for i in list_1:
        if float(i) % 1 == 0:
            list_int.append(int(i))
        else:
            list_float.append(float(i))
    return sorted(list_int) + sorted(list_float)



print(sort_1())