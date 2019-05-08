def fib (n):
    if n < 2:
        return 1
    return fib(n - 1) + fib (n -2) #рекурсія Фібоначі

print (fib(15))

def fact (x):
    if x == 1:
        return 1
    x = x * fact(x - 1)             #рекрсія факторіал
    return x

print (fact(4))

def polindrom (word):
    if len(word) == 1:
        return True
    elif word[0] != word[-1]:
        return False
    return polindrom(word[1:-1])    #рекурсія поліндром

print(polindrom('bajijab'))

def star (w):
    if len(w) == 1:
        return w
    return w[0] + '*' + star(w[1:])

e = 'ALLSTARS'

print(star(e))

def exp (z,c):
    if c == 1:
        return z
    if c < 0:
        z = 1 / exp(z, -c)
    elif c % 2 == 0:
        z = exp(z, c/2) * exp(z, c/2)
    elif c % 2 == 1:
        z = exp(z, c - 1) * exp(z, 1)   #піднесення до степеня
    return z

print(exp(5, -1))