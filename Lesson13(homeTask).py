cycle_list = ('AB', 'CD')

def cycle(*iterable):
    while True:
        for i in iterable:
            for j in i:
                yield from j

g = cycle(cycle_list)
for i in g:
    print(i)