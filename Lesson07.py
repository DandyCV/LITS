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

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
d_2 = {'k1': 5, 'k2': 6, 'k3': 7, 'k4': 8, 'k5': 9}

print(get(d, 'k5', 'key absent'))

def merge(d1, d2):
    d1
    s = set(d1.keys()) & set(d2.keys())
    for k in s:
        d1[k] = d1[k] + d2[k]
    s = set(d2.keys()) - set(d1.keys())
    for k in s:
        d1[k] = d2[k]
    return d1

print(merge(d, d_2))