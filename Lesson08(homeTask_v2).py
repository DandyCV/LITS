def sort_1():
    list_1 = input('Через пробіл введіть числа для сортування: ')
    list_1 = list_1.split()
    list_int = list(filter(lambda x: float(x) % 1 == 0, list_1))
    list_float = list(filter(lambda x: float(x) % 1 != 0, list_1))
    return sorted(list_int) + sorted(list_float)



print(sort_1())