class Stek:
    def __init__(self, stek = []):
        self.stek = stek

    def push(self, new_element):
        print('Додаю в стек елемент ', new_element)
        self.stek.append(new_element)
        return self.stek

    @property
    def pop(self):
        if self.stek:
            print('Видаляю зі стеку елемент ', self.stek.pop())
            return self.stek
        else:
            return 'Стек вже порожній'

    @property
    def length(self):
        return 'Глибина стеку =' + ' ' + str(len(self.stek))

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