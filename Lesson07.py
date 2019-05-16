def func_1(l1, l2):
    return list(set(l1) & set(l2))


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [5, 6, 7, 8, 9, 10, 11, 12]
print(func_1(l1, l2))


def get(d, k, v = None):
    if k in d:
        return d[k]
    else:
        return v


d = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k6':6}
d_2 = {'k1': 5, 'k2': 6, 'k3': 7, 'k4': 8, 'k5': 9, 'k6':2}

print(get(d, 'k5', 'key absent'))


def merge(d1, d2):
    d_merge = {}
    for k in d1:
        d_merge[k] = d1[k]
    s = set(d1.keys()) & set(d2.keys())
    for k in s:
        d_merge[k] = d1[k] + d2[k]
    s = set(d2.keys()) - set(d1.keys())
    for k in s:
        d_merge[k] = d2[k]
    return d_merge


print(merge(d, d_2))