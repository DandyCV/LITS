def mul2(func):
    def inner(*arg):
        r = func(*arg)
        return 2*r
    return inner
@mul2
def f(a, b):    # mul2(f)(3,3)
    return a + b
print(f(3, 3))

def mul(a):
    def inner(b):
        return a + b
    return inner
mul2 = mul(2)
print(mul2(2))

def counter(f):
    count = 0
    def inner(*arg, **kw):
        nonlocal count
        count +=1
        inner.count = count
        return f(*arg, **kw)
    return inner
@counter
def p():
    print('Hi')
p()
p()
p()
print(p.count)

def dec(func):
        def inner(*arg, **kw):
            print (func(*arg, **kw))
        return inner
@dec
def f(x):
    return(x)
f('Hello')

def is_b_zero(f):
    def inner(a, b):
        if b == 0:
            print ('Division by ZERO error')
        else: f(a, b)
    return inner
@is_b_zero
def f(a, b):
    print(a / b)

f(1, 0)