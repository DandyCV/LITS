class Stek:
    '''Стек глибино 5 елементів'''
    def __init__(self, stek = []):
        self.stek = stek

    def push(self, new_element):
        if len(self.stek) < 5:
            print('Додаю в стек елемент ', new_element)
            self.stek.append(new_element)
            return self.stek
        else:
            print('Стек переповнений, елемент ', new_element, ' не додано.')
            return self.stek

    @property
    def pop(self):
        if self.stek:
            print('Видаляю зі стеку елемент ', self.stek.pop())
            return self.stek
        else:
            return 'В стеку не залишилось елементів.'

    @property
    def length(self):
        return 'Глибина стеку = ' + str(len(self.stek))

    @property
    def is_empty(self):
        if self.stek:
            return 'В стеку є елементи'
        else:
            return 'Стек порожній'


print(Stek().push(2))
print(Stek().push('a'))
print(Stek().push(7))
print(Stek().push('j'))
print(Stek().push('11'))
print(Stek().push('k'))
print(Stek().pop)
print(Stek().length)
print(Stek().is_empty)
print(Stek().pop)
print(Stek().pop)
print(Stek().pop)
print(Stek().pop)
print(Stek().pop)
print(Stek().is_empty)
print(Stek().pop)