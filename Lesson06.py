def for_list(list_1):
    list_1_slice = list_1[:]
    for_list = []
    for i in range(len(list_1)):
        n = list_1_slice.pop()
        for_list.append(n)
    return for_list

def add_list(list_1):
    new_list = []
    for i in range(len(list_1)-1,-1,-1):
        new_list.append(list_1[i])
    return new_list


def slice_list(list_1):
    return list_1[::-1]

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(for_list(l))
print(add_list(l))
print(slice_list(l))