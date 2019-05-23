def matrix(n):
    matrix_0 = [[x*0 for x in range(1, n + 1)] for x in range (1, n + 1)]
    return(matrix_0)


def matrix_2(n):
    x = 0
    matrix_0 = [[x]*n]*n
    print(matrix_0)
    matrix_0[0][1] = 1
    return matrix_0

print(matrix(5))
print(matrix_2(4))

def is_prime(i):
    if i == 2: return True
    for n in range(3, i):
        if i % n == 0: return False
    return True


def primes(n):
    list_p = [x for x in range(2,n+1) if is_prime(x)]
    return list_p


print(primes(17))