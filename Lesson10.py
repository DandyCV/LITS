class Rectangle():
    def __init__(self, a, b):
        self.c = a
        self.d = b

    @property
    def prop(self):
        p = 2 * self.c + 2 * self.d
        s = self.c * self.d
        print('Arean = ', s , 'Perimetr =', p)

    @staticmethod
    def stat(a1, b1):
        s = a1 * b1
        p = 2*a1 + 2*b1
        print('S = ', s)
        print('P = ', p)


Rectangle.stat(4, 6)

Rectangle(3, 5).prop