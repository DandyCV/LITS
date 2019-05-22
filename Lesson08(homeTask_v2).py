def sort_1():
    list_1 = input('Через пробіл введіть числа для сортування: ')
    list_1 = list_1.split()
    list_int = []
    list_float = []
    for x in list(filter(lambda x: float(x) % 1 == 0, list_1)):
        list_int.append(int(x))

    for x in list(filter(lambda x: float(x) % 1 != 0, list_1)):
        list_float.append(float(x))
    return sorted(list_int) + sorted(list_float)


print(sort_1())