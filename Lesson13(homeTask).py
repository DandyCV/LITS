cycle_list = ('AB', 'CD')

def cycle(*iterable):
    iterable_list = [x for i in iterable for y in i for x in y]
    while True:
        for i in iterable_list:
            print(i)
        iterable_list.reverse()


print(cycle(cycle_list))