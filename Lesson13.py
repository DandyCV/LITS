# class Gen:
#     lst = [1,2,3]
#     ind = 0
#
#     def __iter__(self):
#         return self.lst
#     def __next__(self):
#         if self.ind < len(self.lst):
#             return self.lst(self.ind)
#         else:
#             raise StopIteration
#     def __contains__(self, value):
#         return value in self.list
#
# #gen = Gen()
# def gen():
#     yield 42
#
# def fib(n):
#     a, b = 0, 1
#     while True:
#         if a <= n:
#             yield a
#             a, b = b, a + b
#         else:
#             break
# f = fib(1000)
# for i in f:
#     print(i)
#
# def chain(*iterable):
#     for it in iterable:
#         for item in it:
#             yield item
#
# for i in chain([1,2,3], {4:4, 5:5}):
#     print(i)

# def seq():
#     n := 0
#     while True
#         yield n
#         n = 4 * n + 3
#
# m = 0
#
# for i in seq():
#     m += i

def gen1():
    n = yield
    while True:
        yield 3 * n -3
        if n >= 10000:
            break


g = gen1()
#print(g.send(None))
for i in g:
    print(i)


