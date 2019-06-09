cycle_list = ('AB', 'CD')

def cycle(*iterable):
    iterable_list = [y for x in iterable for y in x]
    while True:
        for i in iterable_list:
            yield from i

g = cycle(cycle_list)
for i in g:
    print(i)