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

