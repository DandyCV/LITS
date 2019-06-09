cycle_list = ('AB', 'CD')

def cycle(*iterable):
    iterable_list = [x for i in iterable for y in i for x in y]
    while True:
        for i in iterable_list:
            yield i
        iterable_list.reverse()


g = cycle(cycle_list)
for i in g:
    print(i)