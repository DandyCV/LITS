class A:
    a = 'a'

    def print_self(self):
        print('A')


class B:
    b = 'b'

    def print_self(self):
        print('B')


class C(A, B):
    c = 'c'


c = C()
print(c.a, c.b, c.c)
c.print_self()
print(C.mro())

print(dir(C))
print(B.__dict__)


def singltone(cls):
    instance = None

    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singltone
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)
p2 = Point(4, 5)
print(p1 is p2)

import functools


def class_decorator(cls):
    @functools.wraps(cls)
    def iner(*args):
        obj = cls(*args)
        print(obj)
        return (obj)


@class_decorator
class New_class:
    pass


class My_dict(dict):
    def __init__(self, my_dict):
        self.my_dict = my_dict

    # my_dict += {a : a}  += повинно додавати пару ключ : значення у словник
    def __iadd__(self, new_k_v):
        if isinstance(new_k_v, dict) and not isinstance(new_k_v, My_dict):
            return self.my_dict.update(new_k_v)
        return self.my_dict


m = My_dict({'a': 1, 'b': 2})
print(m += {'c': 3})
